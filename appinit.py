# init file

""" Init code
	create new Bottle instant
	init database config
"""
import bottle
import bottle.ext.sqlite
import os

import blogs
import images
from blogconf import blogconf

app = bottle.Bottle()

blogdf = blogconf.get("blogdb", "filename")
imagedf = blogconf.get("imagedb", "filename")

# init database if need
if not os.path.isfile(blogdf):
	blogs.init_db(blogdf)
if not os.path.isfile(imagedf):
	images.init_db(imagedf)

blogdb = bottle.ext.sqlite.Plugin(dbfile=blogdf, keyword="blogdb")
imagedb = bottle.ext.sqlite.Plugin(dbfile=imagedf, keyword="imagedb")
# for some bug reason
blogdb.name = 'blogdb'
imagedb.name = 'imagedb'
app.install(blogdb)
app.install(imagedb)
