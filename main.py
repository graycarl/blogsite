#!\python31\python.exe
# start file of the site

from bottle import run, template, static_file, request, redirect, response
from appinit import app
from datetime import datetime
import users

@app.route("/")
def index(db):
	sqlcmd = "select id, title, posttime from blogs order by posttime desc limit 10;"
	data = db.execute(sqlcmd).fetchall()
	titles = []
	for d in data:
		dic = {}
		dic["id"], dic["title"], dic["posttime"] = d
		titles.append(dic)
	return template("index", titles=titles)

@app.route("/archive")
def archive(db):
	sqlcmd = "select id, title, posttime from blogs"
	data = db.execute(sqlcmd).fetchall()
	arts = {}
	for d in data:
		dic = {}
		dic["id"], dic["title"], dic["posttime"] = d
		dt = datetime.strptime(dic["posttime"], "%Y-%m-%d %H:%M:%S")
		dt = "%s-%s" % (str(dt.year), str(dt.month))
		if dt not in arts.keys():
			arts[dt] = []
		arts[dt].append(dic)
	mons = list(arts.keys()); mons.sort(); mons.reverse()
	return template("archive", arts=arts, mons=mons)

@app.route("/article/<id:int>")
def show_article(id, db):
	sqlcmd = "select author, posttime, title, content from blogs where id=%d;" % id
	author, posttime, title, content = db.execute(sqlcmd).fetchone()
	return template("article", title=title, posttime=posttime, author=author, content=content)

@app.route("/static/<path:path>")
def static_path(path):
	return static_file(path, root="static")

@app.route("/login")
@app.route("/login/<err>")
def user_login(err=""):
	err = (err == "error")
	return template("login_page", with_err=err)

@app.route("/login_check", method="POST")
def login_check():
	username = request.POST.username.strip()
	password = request.POST.password.strip()
	if users.verify_user(username, password):
		users.set_cookie(response)
		redirect("/")
	else:
		redirect("/login/error")
		

@app.route("/new")
def new_article():
	if users.get_login(request):
		artid, author, title, content = ("", users.get_login(request), "", "")
		return template("new_edit", dic = locals())
	else:
		redirect("/login")

@app.route("/edit/<artid:int>")
def edit_article(artid, db):
	if users.get_login(request):
		sqlcmd = "select title,author,content from blogs where id = ?"
		title, author, content = db.execute(sqlcmd, (artid,)).fetchone()
		return template("new_edit", dic=locals())
	else:
		redirect("/login")

@app.route("/save_article", method="POST")
def save_article(db):
	artid = request.POST.get("artid", "").strip()
	artauthor = request.POST.artauthor or "Nobody"
	arttime = str(datetime.now())
	arttitle = request.POST.arttitle or "No Title"
	artcontent = request.POST.artcontent or "<p>No content</p>"
	if artid:
		sqlcmd = "update blogs set title=?, content=? where id=?"
		db.execute(sqlcmd, (arttitle, artcontent, artid))
	else:
		sqlcmd = "insert into blogs (author, posttime, title, content) values (?,datetime(?),?,?)"
		db.execute(sqlcmd, (artauthor, arttime, arttitle, artcontent))
	redirect("/")
	
@app.error(404)
def err_404(error):
	return "<p>The site is being building</p>"
	

run(app, host="localhost", port=8080, debug=True)


