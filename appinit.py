# init file

""" Init code
	create new Bottle instant
	init database config
"""
import bottle
import bottle.ext.sqlite
import os

import blogs
from blogconf import blogconf

app = bottle.Bottle()

dbfile = blogconf.get("db", "filename")

# init database if need
if not os.path.isfile(dbfile):
	blogs.init_db(dbfile)

blogdb = bottle.ext.sqlite.Plugin(dbfile=dbfile)
app.install(blogdb)
