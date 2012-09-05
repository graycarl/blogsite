def init_db(dbfile):
	""" (dbfile) -> none

	init pictures database file, include creating table images.
	@dbfile: database file path
	"""
	import sqlite3
	conn = sqlite3.connect(dbfile)
	
	conn.execute("CREATE TABLE pictures(  \
					id INTEGER PRIMARY KEY,\
					ext TEXT, \
					data BLOB)")
	            
	conn.commit()
	conn.close()
	
def add_picture(db, extstr, data):
	""" (db, extstr, data) -> picture_id

	add new picture to database.
	@extstr: ext name
	@data: picture content data
	@picture_id: reture the id
	"""
	sqlcmd = "insert into pictures (ext, data) values (?,?)"
	db.execute(sqlcmd, (extstr, buffer(data)))
	rowid = db.execute("select last_insert_rowid()").fetchone()
	rowid = int(rowid[0])
	return rowid

def remove_picture(db, id):
	""" (db, imageid) -> success

	remove picture from database
	@imageid: id of the picture to be removed
	@sucess: reture if operation success
	"""
	sqlcmd = "delete from pictures where id=?"
	re = db.execute(sqlcmd, (id,))
	return re.rowcount == 1

def get_picture(db, id):
	""" (db, imageid) -> imagedata

	get picture from database
	@imageid: id of the picture to get
	@imagedata: return the picture content as bytes
	"""
	sqlcmd = "select data from pictures where id=?"
	re = db.execute(sqlcmd, (id,)).fetchone()
	return re[0]
