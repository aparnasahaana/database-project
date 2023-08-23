import sqlite3 #import sqlite3 module
#use the connectMethod that belongs to the sqlite3 Module
dbCon= sqlite3.connect("filmflix.db")
dbCursor=dbCon.cursor()