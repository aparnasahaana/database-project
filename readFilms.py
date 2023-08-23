
from connect import *
def read():
  print("Films print Options\nEnter:\n1. Print details of all films.\n2. Print all films of a particular genre\n3. Print all films of a particular year.\n4. Print all films of a particular rating\n5. Exit.")
  try:
      options=int(input("Enter an option from Film print option\n"))
      if options==1:
       dbCursor.execute("SELECT * FROM tblFilms")
   
      elif options==2:
       field=input("Enter the genre").title()    
       #dbCursor.execute(f"SELECT * FROM tblFilms WHERE genre = '{field}' ")
       s = list(dbCursor.execute(f"SELECT * FROM tblFilms WHERE genre='{field}' "))
       length = len(s)
       #print(f"number of records are {length}")
       if length == 0: print("no such records are available")
       else: dbCursor.execute(f"SELECT * FROM tblFilms WHERE genre = '{field}' ")
       #dbCursor.execute(f"SELECT * FROM tblFilms where genre='Action'")
      elif options==3:
        field=input("Enter the year")    
        s=list( dbCursor.execute(f"SELECT * FROM tblFilms where yearReleased={field}"))
        length=len(s)
        if length==0: print("no such records are available") 
        else: dbCursor.execute(f"SELECT * FROM tblFilms where yearReleased={field}")
      elif options==4:
        field=input("Enter the Rating").upper() 

        s = list(dbCursor.execute(f"SELECT * FROM tblFilms where rating='{field}'"))
        length = len(s)
        if length == 0: print("no such records are available")
        else: dbCursor.execute(f"SELECT * FROM tblFilms where rating='{field}'")
      else: 
        print("no options for print is selected")
        exit
      records=dbCursor.fetchall()   
   
      for aRecord in records:
          print(aRecord)
  except: 
          TypeError: print("Enter correct type of value")
          Exception: print("Error")
        
if __name__=="__main__":
 read()
 dbCon.close()   