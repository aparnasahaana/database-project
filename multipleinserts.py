

from connect import *

import readSongs

import time

 

#subroutine/function

def insertSongs():

    songs = []

 

    # insert data stored in the ist into the songs table in the database

    dbCursor.execute("INSERT INTO songs(Title,Artist,Genre) VALUES (?,?,?)", songs)

    dbCon.commit()# save the data permanently in the table

 

    print(f"{songs[0]} insertd into songs table")

    time.sleep(3)

     # call readSongs.read()

    readSongs.read()

       

if __name__=="__main__":

    insertSongs()

    dbCon.close() # closes the connnection

 

 

 