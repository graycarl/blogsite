#!\python31\python.exe
# main frame of the site

from bottle import run, template, static_file, request, redirect, response, \
		           HTTPError
from appinit import app
from datetime import datetime
import users
import blogs

contype_markdown = blogs.Blog.contype_markdown
contype_html = blogs.Blog.contype_html
status_posted = blogs.Blog.status_posted
status_draft = blogs.Blog.status_draft
status_deleted = blogs.Blog.status_deleted

# Nornal Views
##########################################################################
@app.route("/")
@app.route("/page/<page:int>")
def index(db, page=1):
	num = 3; offset = (page-1)*num
	blog = blogs.get_latest_articles(db, num, offset)
	next = bool(blogs.get_latest_articles(db, num, offset+num))
	return template("index_page", blogs=blog, next=next, page=page)

@app.route("/archive")
def archive(db):
	mons, arts = blogs.get_archive(db)
	return template("archive_page", arts=arts, mons=mons)

@app.route("/article/<id:int>")
def show_article(id, db):
	blog = blogs.get_article(db, id)
	if blog:
		return template("article_page", blog=blog)
	return HTTPError(404, "Page not found")

@app.route("/about")
def show_about():
	return template("about_page")

# Admin Views
###########################################################################
def prepare_admin(request):
	if not users.get_login(request):
		redirect("/login")

@app.route("/login")
@app.route("/login/<err>")
def user_login_page(err=""):
	err = (err == "error")
	return template("login_page", with_err=err)

@app.route("/login_check", method="POST")
def login_check():
	username = request.POST.username.strip()
	password = request.POST.password.strip()
	if users.verify_user(username, password):
		users.set_cookie(response)
		redirect("/admin")
	else:
		redirect("/login/error")

@app.route("/logout")
def logout():
	users.logout(response)
	redirect("/")

@app.route("/admin")
def admin_main(db):
	prepare_admin(request)
	articles = blogs.get_latest_titles(db, 10)
	return template("admin_main_page", blogs=articles)
		
@app.route("/admin/edit/<id:int>")
def admin_edit_article(db, id):
	prepare_admin(request)
	blog = blogs.get_article(db, id)
	return template("admin_newedit_page", blog=blog)

@app.route("/admin/new-article")
def admin_new_article(db, id=""):
	prepare_admin(request)
	id, author, title, content, contype = \
			("", users.get_login(request), "", "", contype_markdown)
	blog = blogs.Blog(**locals())
	if id:
		blog = blogs.get_article(db, id, status=status_draft)
	return template("admin_newedit_page", blog=blog)

@app.route("/admin/post-article", method="POST")
@app.route("/admin/post-article/<id:int>")
def admin_post_article(db, id=None):
	prepare_admin(request)
	if id:
		blogs.update_article(db, id, status=status_posted)
		redirect("/admin")
	else:
		id = request.POST.get("artid", "").strip()
		author = request.POST.artauthor or "Nobody"
		posttime = str(datetime.now())
		title = request.POST.arttitle or "No Title"
		content = request.POST.artcontent or "<p>No content</p>"
		contype = request.POST.artcontype or None
		blog = blogs.Blog(**locals())
		if blog.id:
			blog.id = int(blog.id)
			blogs.update_article(db, blog.id, title=blog.title, \
				content=blog.content, contype=contype,status=status_posted)
		else:
			blogs.add_article(db, blog, status=status_posted)
		redirect("/admin")

@app.route("/admin/draft-article", method="POST")
@app.route("/admin/draft-article/<id:int>")
def admin_draft_article(db, id=None):
	prepare_admin(request)
	if id:
		blogs.update_article(db, id, status=status_draft)
		redirect("/admin/draft")
	else:
		id = request.POST.get("artid", "").strip()
		author = request.POST.artauthor
		posttime = str(datetime.now())
		title = request.POST.arttitle
		content = request.POST.artcontent
		contype = request.POST.artcontype or None
		blog = blogs.Blog(**locals())
		if blog.id:
			blog.id = int(blog.id)
			blogs.update_article(db, blog.id, title=blog.title, \
					content=blog.content, status=status_draft)
		else:
			blogs.add_article(db, blog, status=status_draft)
		redirect("/admin/draft")

@app.route("/admin/draft")
def admin_draft(db):
	prepare_admin(request)
	articles = blogs.get_latest_titles(db, 10, status=status_draft)
	return template("admin_draft_page", blogs=articles)

@app.route("/admin/del/<id:int>")
@app.route("/admin/del/<id:int>/<clean>")
def admin_del_article(db, id, clean=None):
	prepare_admin(request)
	oldurl = request.get("HTTP_REFERER", "/admin")
	if clean and clean.strip() == "clean": 
		ok = blogs.remove_article(db, id)
	else: 
		ok = blogs.update_article(db, id, status=status_deleted)
	if ok: redirect(oldurl)
	else: return HTTPError(404, "Article not found")

@app.route("/admin/recycle")
@app.route("/admin/recycle/page/<page:int>")
def admin_recycle(db, page=1):
	prepare_admin(request)
	count = 10; offset = (page-1)*count
	articles = blogs.get_latest_titles(db, count, offset, \
			status=status_deleted)
	return template("admin_recycle_page", blogs=articles, page=page)

@app.route("/admin/archive")
def admin_archive_page(db):
	prepare_admin(request)
	mons, titles = blogs.get_archive(db)
	return template("admin_archive_page", mons=mons, titles=titles)


# Other Handlers
###########################################################################
@app.error(404)
def err_404(error):
	return "<p>The site is being building</p>"
	
@app.route("/static/<path:path>")
def static_path(path):
	return static_file(path, root="static")

# Run Server with debug mode
###########################################################################
if __name__ == "__main__":
	run(app, host="localhost", port=8080, debug=True, reloader=True)
