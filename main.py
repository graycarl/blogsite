#!\python31\python.exe
# start file of the site

from bottle import run, template, static_file
from appinit import app

@app.route("/")
def index(db):
	sqlcmd = "select id, title, posttime from blogs order by posttime desc limit 10;"
	data = db.execute(sqlcmd).fetchall()
	titles = []
	for d in data:
		dic = {}
		dic["id"] = d[0]
		dic["title"] = d[1]
		dic["posttime"] = d[2]
		titles.append(dic)
	return template("index", titles=titles)

@app.route("/article/<id:int>")
def show_article(id, db):
	sqlcmd = "select author, posttime, title, content from blogs where id=%d;" % id
	author, posttime, title, content = db.execute(sqlcmd).fetchone()
	return template("article", title=title, posttime=posttime, author=author, content=content)

@app.route("/static/<path:path>")
def static_path(path):
	return static_file(path, root="static")

run(app, host="localhost", port=8080, debug=True)


