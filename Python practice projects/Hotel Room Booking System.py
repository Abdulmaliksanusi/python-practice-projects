#1.Set up books

def setUp():
    books = ["Available"] * 10
    return books

#2.Display Books

def displayBooks(books):
    for x in range(len(books)):
        print("Book", x+1, "-", books[x])

#3.Loan books

def loanBook(books):
    while True:
        userInput = input("Enter the number of the book you want to loan: ")
        if userInput == "":
            print("Try again, the field cannot be left blank")
            continue
        if not userInput.isdigit():
            print("Try again , the value you enter has to be a numerical character")
            continue

        book = int(userInput)
        
        if book < 1 or book > 10:
            print("Try again, out of range the number must be between 1 and 10")
            continue
        else:
            break

    if books[book - 1] == "Available":
        books[book - 1] = "On loan"
        print("The book has now being sucessfully loaned to you")
    else:
        print("The book is already on loan")


#4.Return a book

def returnBook(books):
    while True:
        userInput = input("Enter the number of the book you want to return: ")
        if userInput == "":
            print("Try again, the field cannot be left blank")
            continue
        if not userInput.isdigit():
            print("Try again , the value you enter has to be a numerical character")
            continue
        
        book = int(userInput)
        
        if book < 1 or book > 10:
            print("Try again, out of range the number must be between 1 and 10")
            continue
        else:
            break


    if books[book - 1] == "On loan":
        books[book - 1] = "Available"
        print("The book has now being sucessfully returned!")
    else:
        print("The book was already available")


#5.Check Book Status

def bookStatus(books):
    while True:
        userInput = input("Enter the number of the book you are looking for: ")
        if userInput == "":
            print("Try again, the field cannot be left blank")
            continue
        if not userInput.isdigit():
            print("Try again, the value you enter has to be a numerical character")
            continue
        
        book = int(userInput)
        
        if book < 1 or book > 10:
            print("Try again, out of range the number must be between 1 and 10")
            continue
        else:
            break

    if books[book - 1] == "On loan":
        print("The book you are looking for is not available")
    else:
        print("The book you are looking for is available")
     
#6.Show Statistics

def showStatistics(books):
    onLoan = "On loan"
    available = "Available"

    print("The number of books on loan:",books.count(onLoan))
    print("The number of books available:",books.count(available))

#7.Menu system

def display(books):
    while True:
        print("---Library book menu---")
        print("1.View Books")
        print("2.Loan Books")
        print("3.Return Books")
        print("4.Check Book status")
        print("5.Show Statistics")
        print("6.Exit")

        userChoice = input("Enter the number:")

        if userChoice == "1":
            displayBooks(books)
            continue
        elif userChoice == "2":
            loanBook(books)
            continue
        elif userChoice == "3":
            returnBook(books)
            continue
        elif userChoice == "4":
            bookStatus(books)
            continue
        elif userChoice == "5":
            showStatistics(books)
            continue
        elif userChoice == "6":
            print("Have a good day!")
            break
        else:
            print("Invalid choice")

def main():
    books = setUp()
    display(books)
    
main()
            
            
            
            
            
        

        
    
    
        
