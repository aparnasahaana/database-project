# import CRUD modules
import readFilms, addFilms, updateFilms, deleteFilms 

# create a subroutine/function
def menuOptions():
    options = 0 # flag variable
    menuNumbers = "Films Menu Options\nEnter:\n1. Print.\n2. Add\n3. Update.\n4. Delete.\n5. Exit."
    optionsList = ["1", "2", "3","4", "5"]

    while options not in optionsList: # ["1", "2", "3","4", "5"]# execute the inde code below
        print(menuNumbers)

        # re-assign the value of options
        options = input("Enter an option from the Films main menu!: ")

        if options not in optionsList:# ["1", "2", "3","4", "5"]
            print(f"{options} is not a valid choice in the Film menu!")
    return options


# create a boolean variable 
mainProgram = True

while mainProgram: #Same as while True
    # call/invoke the menuOptions function and assign to a variable 
    mainMenu = menuOptions()
    if mainMenu == "1": # go into the file and call/invoke the respective function
        readFilms.read()
    elif mainMenu =="2":
        addFilms.insertFilms()
    elif mainMenu =="3":
        updateFilms.update()
    elif mainMenu == "4":
        deleteFilms.delete()
    else:
        # re-assign the mainProgram a false Boolean variable 
        mainProgram = False
input("Press enter to quit the Films application")

    

    







# menuOptions()