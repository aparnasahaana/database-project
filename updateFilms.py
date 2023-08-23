"""from connect import *
def update():
    idField=input("Enter song id of the record to update:")
    fieldName=input("Enter Title or Artist or Genre as the Field Name :").title()
    fieldValue=input("Enter the value for '{fieldName}' field: ")
    print(fieldValue)
    fieldValue = "'" + fieldValue + "'"
    print(fieldValue)
    dbCursor.execute("UPDATE songs SET {fieldName}={fieldValue} WHERE SongID = {idField}")
    dbCon.commit()
    print(f"Record {idField} updated in songs table")
if __name__=="__main__":
 update()
"""
from connect import *

#subroutine function
def update():
    # Use the FilmID(primary key) to select and update a record in DB table
    idField = input("Enter FilmID of the record to be updated: ")

    #fieldName: set the field/column(Title or Artist or Genre) to updated
    fieldName = input("Enter Title or YearReleased or Rating or Duration or Genre as the field name: ").title()
    
    #fieldValue: set the field/value for(Title or Artist or Genre) to updated
    fieldValue = input(f"Enter the value for {fieldName} field: ")
    # print(fieldValue)

    fieldValue = "'" +fieldValue+ "'" # add single quote one either of the value
    # print(fieldValue)

    #Update the records in songs table
    "  UPDATE songs SET Title/Artist/Genre = TitleValue/ArtistValue/GenreValue WHERE SongID = 1/2/3/5...."
    dbCursor.execute(f"UPDATE tblFilms SET {fieldName} = {fieldValue} WHERE filmID = {idField}")
    dbCon.commit()

    print(f"Record {idField} updated in tblFilms table")
if __name__=="__main__":
    update()
    dbCon.close()








