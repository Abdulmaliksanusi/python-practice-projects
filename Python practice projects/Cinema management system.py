#Sets up dictionary "bookings"
def setUp():
    bookings = {
        "Avatar": 0,
        "Wonka": 0,
        "Spider-Man": 0,
        "Matilda": 0,
        "Shrek": 0
        }
    return bookings

#Displays the film names and ticket booking amounts
def displayFilms(bookings):
    for film in bookings :
        print(film , "-", bookings[film])

#Adds tickets if the film name entered by the user is valid
def addTickets(bookings):
    while True:
        userInput = input("Enter the name of the film: ")
        if userInput == "":
            print("Try again , the field cannot be left blank")
            continue
        if not userInput.isalpha():
            print("Try again , letetrs only")
            continue
        
        filmName = userInput.capitalize()
        
        if filmName not in bookings:
            print("Error, the name of the film is invalid!")
            continue
        else:
            break

    while True:
        userInput = input("Enter the ticket booking amounts: ")
        if userInput == "":
            print("Try again , the field cannot be left balnk")
            continue
        if not userInput.isdigit():
            print("Try again , numerical characters only")
            continue

        ticketAmounts = int(userInput)

        if ticketAmounts < 0:
            print("The number you entered can't be less than 0")
            continue
        else:
            break

    bookings[filmName] = bookings[filmName] + ticketAmounts
    print("The film bookings has been increased sucessfully")

#Decreases tickiets if the film name is valid and also lesser than the old booking amount
def cancelTickets(bookings):
    while True:
        userInput = input("Enter the name of the film: ")
        if userInput == "":
            print("Try again , the field cannot be left blank")
            continue
        if not userInput.isalpha():
            print("Try again , letetrs only")
            continue
        
        filmName = userInput.capitalize()
        
        if filmName not in bookings:
            print("Error, the name of the film is invalid!")
            continue
        else:
            break

    while True:
        userInput = input("Enter how many tickets your cancelling: ")
        if userInput == "":
            print("Try again , the field cannot be left balnk")
            continue
        if not userInput.isdigit():
            print("Try again , numerical characters only")
            continue

        ticketAmounts = int(userInput)

        if ticketAmounts > bookings[filmName]:
            print("The number you entered can't be less than the old ticket amount")
            continue
        else:
            break

    bookings[filmName] = bookings[filmName] - ticketAmounts
    print("The film bookings has been decreased sucessfully")

#Checks if the film name been searched for is valid and displays the name and number of tickets booked for that film 
def checkFilmBookings(bookings):
     while True:
         userInput = input("Enter the name of the film: ")
         if userInput == "":
             print("Try again , the field cannot be left blank")
             continue
         if not userInput.isalpha():
             print("Try again , letetrs only")
             continue
            
         filmName = userInput.capitalize()

         if filmName not in bookings:
             print("Error, the name of the film is invalid!")
             continue
         else:
             break
            
     print("The number of tickets booked for this film:",filmName,"-",bookings[filmName])

#Display the total number of tickets booked, the film with the highest bookings, the film with the lowest bookings,and the average number of tickets booked
def showStatistics(bookings):
    total = sum(bookings.values())
    lenTotal = len(bookings)
    avg = total/lenTotal
    highestBookings = max(bookings, key=bookings.get)
    lowestBookings = min(bookings, key=bookings.get)

    print("The total number of tickets booked:",total)
    print("The film with the highest bookings:", highestBookings,"-",bookings[highestBookings])
    print("The film with the lowest bookings:", lowestBookings, "-", bookings[lowestBookings])
    print("The average number of tickets booked:", avg)

#Menu 
def menuSystem(bookings):
    while True:
        print("-------------------------------------------------------")
        print("-------------------------MENU--------------------------")
        print("-------------------------------------------------------")
        print("1.View Films")
        print("2.Add Tickets")
        print("3.Cancel Tickets")
        print("4.Check Film Bookings")
        print("5.Show Statistics")
        print("6.Exit")

        choice = input("Enter your number selection: ")

        if choice == "1":
            displayFilms(bookings)
            continue
        elif choice == "2":
            addTickets(bookings)
            continue
        elif choice == "3":
            cancelTickets(bookings)
            continue
        elif choice == "4":
            checkFilmBookings(bookings)
            continue
        elif choice == "5":
            showStatistics(bookings)
            continue
        elif choice == "6":
            print("Have a good day!")
            break
        else:
            print("Invalid choice")

#Calls the set up function in a variable "bookings" and calls the menu function 
def main():
    bookings = setUp()
    menuSystem(bookings)
main()
    
        
    

    
    



    
