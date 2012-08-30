from datetime import datetime
import markdown


class Blog(object):
	""" data struct for an article
	
	id for int id
	author for string
	posttime for string
	title for string
	content for string
	status for status code: [ 0 None, 1 Draft, 2 posted, 3 deleted ]
	comments for comment list
	tags for tag list
	"""
	status_none = "none"
	status_draft = "draft"
	status_posted = "posted"
	status_deleted = "deleted"
	contype_html = "html"
	contype_markdown = "markdown"
	_attrs = ["id", "author", "posttime", "title", "content", \
			"contype", "status", "commects", "tags"]

	def __init__(self, **dic):
		for at in self._attrs:
			self.__setattr__(at, dic.get(at, None))

	@property
	def html(self):
		if self.contype == self.contype_html:
			return self.content
		elif self.contype == self.contype_markdown:
			return markdown.markdown(self.content, \
					['codehilite(guess_lang=False, force_linenos=False)'])
		return None

	@property
	def markdown(self):
		if self.contype == self.contype_markdown:
			return self.content
		return None


def init_db(dbfile):
	""" (dbfile) -> none
	
	init database file, include creating file and creating tables.
	@dbfile: database file path
	"""
	import sqlite3
	conn = sqlite3.connect(dbfile)
	conn.execute("CREATE TABLE blogs ( \
					id INTEGER PRIMARY KEY, \
	        		author char(56) NOT NULL, \
	        		posttime char(20) NOT NULL, \
	        		title TEXT, content TEXT, contype TEXT, \
	                status INTEGER);\
	        	")
	author = "CarlWolf"
	posttime = str(datetime.strptime("2012-3-29 20:34:29","%Y-%m-%d %H:%M:%S"))
	title = "The first article"
	content = "<h2>1. First Article</h2><p>This is the first article</p>"
	contype = Blog.contype_html
	status = Blog.status_posted
	insertcmd = "INSERT INTO blogs \
					(author, posttime, title, content, contype, status) \
	                VALUES (?, datetime(?), ?, ?, ?, ?)"
	conn.execute(insertcmd, 
			(author, posttime, title, content, contype, status))
	
	posttime = str(datetime.strptime("2012-4-29 20:34:29","%Y-%m-%d %H:%M:%S"))
	title = "The second article"
	content = "<h2>1. Second Article</h2><p>This is the second article</p>"
	conn.execute(insertcmd, 
			(author, posttime, title, content, contype, status))

	posttime = str(datetime.strptime("2012-4-9 20:34:29","%Y-%m-%d %H:%M:%S"))
	title = "The third article"
	content = "<h2>1. Third Article</h2><p>This is the third article</p>"
	conn.execute(insertcmd, 
			(author, posttime, title, content, contype, status))

	posttime = str(datetime.strptime("2011-9-29 20:34:29","%Y-%m-%d %H:%M:%S"))
	title = "Welcome to my blog"
	content = "<h2>1. Test Article</h2><p>This is the second article</p>"
	conn.execute(insertcmd, 
			(author, posttime, title, content, contype, status))

	posttime = str(datetime.strptime("2012-7-29 20:34:29","%Y-%m-%d %H:%M:%S"))
	title = "This just a test"
	content = "##This is markdown article\nthis is some paragragh\nnext line"
	contype = Blog.contype_markdown
	conn.execute(insertcmd, 
			(author, posttime, title, content, contype, status))

	conn.commit()
	conn.close()
	
	
def get_latest_titles(db, num, offset=0, status=Blog.status_posted):
	""" (db, num) -> list(blog)

	get latest num article titles 
	"""
	sqlcmd = "select id, title, posttime from blogs \
			where status=? order by posttime desc limit ? offset ?;"
	data = db.execute(sqlcmd, (status, num, offset)).fetchall()
	titles = []
	for d in data:
		b = Blog(id=d[0], title=d[1], posttime=d[2]); 
		titles.append(b)
	return titles

def get_latest_articles(db, num, offset=0):
	""" (db, num) -> list(blog)

	get latest num articles
	"""
	sqlcmd = "select id, title, posttime, content, contype from blogs \
			where status=? order by posttime desc limit ? offset ?;"
	data = db.execute(sqlcmd, (Blog.status_posted, num, offset)).fetchall()
	articles = []
	for d in data:
		b = Blog(id=d[0], title=d[1], posttime=d[2], content=d[3], \
				contype=d[4]); 
		articles.append(b)
	return articles

def get_archive(db):
	""" (db) -> (list(datestr), dic(datestr, list(blog)))

	get all the articles' titles, group them into year-month, 
	and then return with reverse sort. 
	"""
	sqlcmd = "select id, title, posttime from blogs where status=?"
	data = db.execute(sqlcmd, (Blog.status_posted,)).fetchall()
	arts = {}
	for d in data:
		b = Blog(id=d[0], title=d[1], posttime=d[2])
		dt = datetime.strptime(b.posttime, "%Y-%m-%d %H:%M:%S")
		dt = "%s-%s" % (str(dt.year), str(dt.month))
		if dt not in arts:
			arts[dt] = []
		arts[dt].append(b)
	mons = list(arts.keys()); mons.sort(); mons.reverse()
	return mons, arts

def get_article(db, id, status=None):
	""" (db, id, status=None) -> blog

	return the article with the specified id and status. 
	"""
	if status != None:
		sqlcmd = "select author, posttime, title, content, contype \
				from blogs where id=%d and status=%d;" % (id, status)
	else:
		sqlcmd = "select author, posttime, title, content, contype \
				from blogs where id=%d;" % id
	data = db.execute(sqlcmd).fetchone()
	if not data:
		return None
	b = Blog(id=id, author=data[0], posttime=data[1], title=data[2], \
				content=data[3], contype=data[4]);
	return b

def remove_article(db, id):
	""" (db, id) -> success

	delete the article with specified id.
	return True for success, False for failed.
	"""
	sqlcmd = "delete from blogs where id = ?"
	re = db.execute(sqlcmd, (id,))
	return re.rowcount == 1

def add_article(db, blog, status=Blog.status_posted):
	""" (db, blog, status=Blog.status_posted) -> success

	add new article to database.
	return True for success, False for failed.
	"""
	sqlcmd = "insert into blogs \
			(author, posttime, title, content, contype, status) \
			values (?, datetime(?), ?, ?, ?, ?)"
	blog.status = status
	re = db.execute(sqlcmd, (blog.author, blog.posttime, blog.title, \
						blog.content, blog.contype, blog.status))
	return re.rowcount == 1

def update_article(db, id, **dic):
	""" (db, id, **dic) -> success

	update some attribute of an article.
	only `title, content, status` are allowed.
	return True for success, False for failed.
	"""
	namestr = []
	values = []
	for attr in ("title", "content", "status", "contype"):
		if attr in dic: 
			namestr.append(attr+"=?")
			values.append(dic[attr])
	if not namestr:
		return False
	namestr = ", ".join(namestr)
	sqlcmd = "update blogs set %s where id=%d" % (namestr, id)
	re = db.execute(sqlcmd, values)
	return re.rowcount == 1
