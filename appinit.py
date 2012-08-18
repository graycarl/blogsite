# init file

""" Init code
	create new Bottle instant
	init database config
"""
import bottle
import bottle.ext.sqlite
import os

import blogs

app = bottle.Bottle()

dbfile = "database/blogs.db"

# init database if need
if not os.path.isfile(dbfile):
	blogs.init_db(dbfile)

blogdb = bottle.ext.sqlite.Plugin(dbfile=dbfile)
app.install(blogdb)
