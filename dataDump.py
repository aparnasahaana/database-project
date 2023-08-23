"""from connect import*
import readSongs
import time

def bulkInsert():
    with open(r"Pt9_10DB\songs.sql")as sqlFile:
        dumpData=sqlFile.read()
        dbCursor.executescript(dumpData)
        dbCon.commit()
        time.sleep(3)
        readSongs.read()"""
from connect import *
import readSongs
import time


#subroutine/function
def bulkInsert():
    # load script (songs.sql) from file and save it to sqlFile
    with open(r"songs.sql") as sqlFile:
        # read content in alias (sqlFile) and save into dumpData variable 
        dumpData = sqlFile.read()

        #call/invoke the executescript method and pass dumpData as an argument 
        dbCursor.executescript(dumpData)
        dbCon.commit()

        time.sleep(3)

        # call readSongs.read()
        readSongs.read()
        
if __name__=="__main__":
    bulkInsert()