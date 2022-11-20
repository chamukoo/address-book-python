# Programmed by: Lee Anne Angeles and Charina Vallecera

contactsList = [" "]
firstnames = []
lastnames = []
addresses = []
numbers = []


def mainMenu():
    print("\n<<<<<<<<<<<<<<<<<< MAIN MENU >>>>>>>>>>>>>>>>>>>")
    print("What would you like to do?")
    print("[1] Add Contact")
    print("[2] Edit Contact")
    print("[3] Delete Contact")
    print("[4] View Contact")
    print("[5] Search Address Book")
    print("[6] Exit")


def tabulation():
    print(" ")
    print('=' * 137)
    print(f"\t{'ENTRY': <15s}{'FIRST NAME': <20s}{'LAST NAME': <20s}{'COMPLETE ADDRESS': <60s}{'PHONE NUMBER': <15s}")
    print('=' * 137)


def viewContact():
    contactsList.pop(0)
    counter = 0
    tabulation()

    for a in contactsList:
        counter += 1
        print("\t" + str(counter) + a)
        print('-' * 137)
    contactsList.insert(0, "")
    return contactsList


def addContact():
    while True:
        print("\n<<<<<<<<<<<<<<<<< ADD CONTACT >>>>>>>>>>>>>>>>>>>")
        first = input("First Name: ")
        firstnames.append(first)
        last = input("Last Name: ")
        lastnames.append(last)
        address = input("Complete Address: ")
        addresses.append(address)
        phone = input("Contact Number: ")
        numbers.append(phone)
        contact = f"\t\t\t\t{first: <20}{last: <20}{address: <60}{phone: <15}"
        contactsList.append(contact)
        print("The contact has been successfully added!")

        while True:
            addAgain = input("\nWould you like to add another contact? [ yes / no ] : ")
            if addAgain.casefold() == "yes":
                break
            elif addAgain.casefold() == "no":
                runProgram()
            else:
                print("Invalid Input! Please try again!")
                continue


def editContact():
    while True:
        print("\n<<<<<<<<<<<<<<<< EDIT CONTACT >>>>>>>>>>>>>>>>>>>")
        modify = int(input("Enter the entry number you want to modify: "))
        contactsList.pop(modify)
        first = input("Enter New First Name: ")
        last = input("Enter New Last Name: ")
        address = input("Enter New Address: ")
        phone = input("Enter New Contact Number: ")
        modifiedContact = f"\t\t\t\t{first: <20s}{last: <20s}{address: <60s}{phone: <15s}"
        contactsList.insert(modify, modifiedContact)
        print("Modification saved!\nPlease go to 'VIEW CONTACT' to see the edited information.\n")

        while True:
            editAgain = input("Would you like to edit another contact? [ yes / no ] : ")
            if editAgain.casefold() == "yes":
                break
            elif editAgain.casefold() == "no":
                runProgram()
            else:
                print("Invalid Input! Please try again!")
                continue


def deleteContact():
    while True:
        print("\n<<<<<<<<<<<<<<<< DELETE CONTACT >>>>>>>>>>>>>>>>>")
        index = int(input("Enter the entry number you want to delete: "))
        contactsList.pop(index)
        print("The contact has been successfully deleted!")
        print("Please go to 'VIEW CONTACT' to see the updated contact lists.\n")

        while True:
            deleteAgain = input("Would you like to delete another contact? [ yes / no ] : ")
            if deleteAgain.casefold() == "yes":
                break
            elif deleteAgain.casefold() == "no":
                runProgram()
            else:
                print("Invalid Input! Please try again!")
                continue


def searchContact():
    while True:
        print("\n<<<<<<<<<<<<<<< SEARCH CONTACT >>>>>>>>>>>>>>>>")
        print("What information do you want to search on?")
        print("[a] First Name")
        print("[b] Last Name")
        print("[c] Address")
        print("[d] Contact Number")
        searchOption = input("Choose the letter corresponding to your choice: ")

        if searchOption.casefold() == 'a':
            searchFirst = input("\nEnter First Name: ")
            counter = 0
            tabulation()
            for contacts in contactsList:
                if searchFirst in contacts:
                    if searchFirst in firstnames:
                        index = contactsList.index(contacts)
                        print("\t" + str(index) + contacts)
                        print('-' * 137)
                        counter += 1

            if searchFirst in firstnames:
                print("\nSuccessfully found the contact/s!")

            if searchFirst not in firstnames:
                print(f"\t{'---': <15s}{'---': <20s}{'---': <20s}{'---': <60s}{'---': <15s}")
                print('-' * 137)
                print("No contact found with the provided first name: {}".format(searchFirst))

        elif searchOption.casefold() == 'b':
            searchSurname = input("\nEnter Surname: ")
            counter = 0
            tabulation()
            for contacts in contactsList:
                if searchSurname in contacts:
                    if searchSurname in lastnames:
                        index = contactsList.index(contacts)
                        print("\t" + str(index) + contacts)
                        print('-' * 137)
                        counter += 1

            if searchSurname in lastnames:
                print("\nSuccessfully found the contact/s!")

            if searchSurname not in lastnames:
                print(f"\t{'---': <15s}{'---': <20s}{'---': <20s}{'---': <60s}{'---': <15s}")
                print('-' * 137)
                print("\nNo contact found with the provided last name: {}".format(searchSurname))

        elif searchOption.casefold() == 'c':
            searchAddress = input("\nEnter Address: ")
            counter = 0
            tabulation()
            for contacts in contactsList:
                if searchAddress in contacts:
                    if searchAddress in addresses:
                        index = contactsList.index(contacts)
                        print("\t" + str(index) + contacts)
                        print('-' * 137)
                        counter += 1

            if searchAddress in addresses:
                print("\nSuccessfully found the contact/s!")

            if searchAddress not in addresses:
                print(f"\t{'---': <15s}{'---': <20s}{'---': <20s}{'---': <60s}{'---': <15s}")
                print('-' * 137)
                print("\nNo contact found with the provided address: {}'".format(searchAddress))

        elif searchOption.casefold() == 'd':
            searchPhone = input("\nEnter Contact Number: ")
            counter = 0
            tabulation()
            for contacts in contactsList:
                if searchPhone in contacts:
                    if searchPhone in numbers:
                        index = contactsList.index(contacts)
                        print("\t" + str(index) + contacts)
                        print('-' * 137)
                        counter += 1

            if searchPhone in numbers:
                print("\nSuccessfully found the contact/s!")

            if searchPhone not in numbers:
                print(f"\t{'---': <15s}{'---': <20s}{'---': <20s}{'---': <60s}{'---': <15s}")
                print('-' * 137)
                print("\nNo contact found with the provided contact number: {}".format(searchPhone))
        else:
            print("Invalid Input! Please try again!")
            searchContact()

        while True:
            searchAgain = input("\nWould you like to search another contact? [ yes / no ] : ")
            if searchAgain.casefold() == "yes":
                break
            elif searchAgain.casefold() == "no":
                runProgram()
            else:
                print("Invalid Input! Please try again!")
                continue


def exitProgram():
    while True:
        print("\n<<<<<<<<<<<<<<<<<<<<<<< EXIT PROGRAM >>>>>>>>>>>>>>>>>>>>>>>>>")
        exitOption = input("Are you sure you want to close this program? [ yes / no ] : ")
        if exitOption.casefold() == "yes":
            print("Thank you for using this program!")
            print("Bye!")
            exit()
        elif exitOption.casefold() == "no":
            runProgram()
        else:
            print("Invalid Input! Please try again!")
            continue


def runProgram():
    while True:
        mainMenu()
        menuOption = input("Choose the number corresponding to your choice: ")

        if menuOption in ('1', '2', '3', '4', '5', '6'):
            if menuOption == '1':
                addContact()
            elif menuOption == '2':
                editContact()
            elif menuOption == '3':
                deleteContact()
            elif menuOption == '4':
                viewContact()
                runProgram()
            elif menuOption == '5':
                searchContact()
            elif menuOption == '6':
                exitProgram()
        else:
            print("Invalid Input! Please choose a number on the menu and try again!")
            continue


while True:
    runProgram()
