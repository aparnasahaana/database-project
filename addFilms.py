from connect import *
import time
def insertFilms():
    tblFilms=[]#create an empty list
   # SongID,Title,Artist,Genre
   #SongID is AUTOINCREMENT and numeric value will be added automatically string from 1
    title=input("Enter Film Title:").title()

    yearReleased=input("Enter the year Released:")
    rating=input("Enter Film rating:").upper()

    duration=input("Enter the Film duration:")
    genre=input("Enter Fim Genre:").title()
    tblFilms.append(title)
    tblFilms.append(yearReleased)
    tblFilms.append(rating)
    tblFilms.append(duration)
    tblFilms.append(genre)
    dbCursor.execute
# insert data stored in the ist into the songs table in the database

    dbCursor.execute("INSERT INTO tblFilms(Title,YearReleased,Rating,Duration,Genre) VALUES (?,?,?,?,?)",tblFilms)
    #dbCursor.execute INSERT INTO FilmTable
    #     #dbCon.commit()
    dbCon.commit()# save the data permanently in the table
    print(f"{title} insertd into FilmTable")

if __name__=="__main__":

 insertFilms() 
 dbCon.close()   