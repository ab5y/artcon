import sqlite3
import os

DATABASE = os.path.join('.', 'artcon.db')
SCHEMA = os.path.join('.', 'schema.sql')

def connect_db():
	return sqlite3.connect(DATABASE)

def init_db():
	con = connect_db()
	cur = con.cursor()
	f = open('.\schema.sql', 'r')
	sql = f.read()
	cur.executescript(sql)
	print 'Success!'

init_db()