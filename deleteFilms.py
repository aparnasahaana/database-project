from connect import *


#subroutine function
def delete():
    # Use the SongID(primary key) to select and delete a record in DB table
    idField = input("Enter FilmID of the record to be deleted: ")

    "DELETE FROM songs WHERE SongID = 1/2/3/4/5....."
    dbCursor.execute(f"DELETE FROM tblFilms WHERE filmID = {idField}")
    dbCon.commit()

    print(f"Record {idField} deleted from tblFilms table")
    
if __name__=="__main__":
    delete()
    dbCon.close() # closes the connnection