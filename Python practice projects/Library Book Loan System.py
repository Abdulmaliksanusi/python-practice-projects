#Sets up dictionary
def setUp():
    loans = {
        "Holes": 0,
        "Wonder": 0,
        "Macbeth": 0,
        "1984": 0,
        "Coraline": 0
        }
    return loans

#Displays the book name and their loan amounts
def displayBooks(loans):
    for book in loans:
        print(book , "-", loans[book])

#Increases the book loan value if the book name is valid 
def addLoan(loans):
    while True:
        userInput = input("Enter book name: ")
        if userInput == "":
            print("Try again , the field can't be left blank")
            continue
        if not userInput.isalpha():
            print("Try again , letters only")
            continue

        bookName = userInput.capitalize()

        if bookName not in loans:
            print("Error , the book name does not exist")
            continue
        else:
            break

    while True:
        userInput = input("Enter how many copies has been loaned out: ")
        if userInput == "":
            print("Try again , the field cannot be left blank")
            continue
        if not userInput.isdigit():
            print("Try again , numerical characters only")
            continue

        loanValue = int(userInput)

        if loanValue < 0:
            print("The number entered can't be less than 0")
            continue
        else:
            break

    loans[bookName] = loans[bookName] + loanValue
    print("The book loan value has been increased sucessfully")

#Decreases the book loan value if the book name is valid and also if the value is lesser that the old value  
def removeLoan(loans):
     while True:
        userInput = input("Enter book name: ")
        if userInput == "":
            print("Try again , the field can't be left blank")
            continue
        if not userInput.isalpha():
            print("Try again , letters only")
            continue

        bookName = userInput.capitalize()

        if bookName not in loans:
            print("Error , the book name does not exist")
            continue
        else:
            break

     while True:
         userInput = input("Enter how mnay copies has been removed: ")
         if userInput == "":
             print("Try again , the field cannot be left blank")
             continue
         if not userInput.isdigit():
             print("Try again , numerical characters only")
             continue

         loanValue = int(userInput)

         if loanValue > loans[bookName]:
             print("The number entered can't be less than the old value")
             continue
         else:
             break

     loans[bookName] = loans[bookName] - loanValue
     print("The book loan value has been removed sucessfully")

#Checks if the book the user is searching for exists and if it exists ,displays the book name and the loan value
def checkBookLoans(loans):
    while True:
        userInput = input("Enter book name: ")
        if userInput == "":
            print("Try again , the field can't be left blank")
            continue
        if not userInput.isalpha():
            print("Try again , letters only")
            continue

        bookName = userInput.capitalize()

        if bookName not in loans:
            print("Error , the book name does not exist")
            continue
        else:
            break
    print("The number of copies currently on loan for",bookName,"is",loans[bookName])

#Displays the total number of books currently on loan, the book with the highest number on loan, the book with the lowest number on loan, and the average number on loan
def showStatistics(loans):
    total = sum(loans.values())
    lenTotal = len(loans)
    avg = total/lenTotal
    highestNumberOnLoan = max(loans,key=loans.get)
    lowestNumberOnLoan = min(loans,key=loans.get)
    
    print("The total number of books currently on loan:",total)
    print("The book with the highest number on loan:",highestNumberOnLoan,"-",loans[highestNumberOnLoan])
    print("The book with the lowest number on loan:",lowestNumberOnLoan,"-",loans[lowestNumberOnLoan])
    print("The average number on loan:",avg)
    
#Menu        
def menuSystem(loans):
    while True:
        print("-------------------------------------------------------------")
        print("-------------------------MENU-----------------------------")
        print("-------------------------------------------------------------")#
        print("1.View Books")
        print("2.Add loans")
        print("3.Return Books")
        print("4.Check Book Loans")
        print("5.Show Statistics")
        print("6.Exit")

        choice = input("Enter your number selection: ")
        if choice == "1":
            displayBooks(loans)
            continue
        elif choice == "2":
            addLoan(loans)
            continue
        elif choice == "3":
            removeLoan(loans)
            continue
        elif choice == "4":
            checkBookLoans(loans)
            continue
        elif choice == "5":
            showStatistics(loans)
            continue
        elif choice == "6":
            print("Have a good day!")
            break
        else:
            print("Invalid choice")
            
#Calls the set up function in the variable "loans" and also calls the menu function 
def main():
    loans = setUp()
    menuSystem(loans)
main()

    
