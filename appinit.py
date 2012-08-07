# init file

""" Init code
	create new Bottle instant
	init database config
"""
import bottle
import bottle.ext.sqlite
import os

app = bottle.Bottle()

# init database if need
if not os.path.isfile("database/blogs.db"):
	import sqlite3
	import datetime
	conn = sqlite3.connect("database/blogs.db")
	conn.execute("CREATE TABLE blogs ( \
					id INTEGER PRIMARY KEY, \
	        		author char(56) NOT NULL, \
	        		posttime char(20) NOT NULL, \
	        		title TEXT, content TEXT);\
	        	")
	conn.execute("INSERT INTO blogs \
					(author, posttime, title, content) \
	                VALUES \
	                (?,datetime(?),?,?)", \
	             	("Carl Wolf", \
	                  str(datetime.datetime.strptime("2012-3-29 20:12:23", "%Y-%m-%d %H:%M:%S")), \
	                  "this is a title", \
	                  "<h3>This is a test artical</h3><p>this is test content</p>"
	                )
	            )
	conn.commit()
	conn.close()


blogdb = bottle.ext.sqlite.Plugin(dbfile="database/blogs.db")
app.install(blogdb)