
#1.Set Up Rooms

def setUp():
    rooms = ["Available"] * 12
    return rooms

#2.Display Rooms

def displayRooms(rooms):
    for x in range(len(rooms)):
        print("Room", x+1, "-", rooms[x])

#3.Book a Room

def bookRoom(rooms):
    while True :
        userInput = input("Enter the room you want to book: ")
        if userInput == "":
            print("Try again, the field cannot be left blank")
            continue
        if not userInput.isdigit():
            print("Try again , the value you enter has to be a numerical character")
            continue
        
        room = int(userInput)

        if room < 1 or room > 12:
            print("Try again , the room number ranges from 1 - 12")
            continue
        else:
            break

    if rooms[room - 1] == "Available":
        rooms[room - 1] = "Booked"
        print("The hotel room you want as being sucessfully booked")
    else:
        print("The room is already booked")


#4.Cancel a Booking

def cancelBooking(rooms):
    while True :
        userInput = input("Enter the room you want to cancel booking: ")
        if userInput == "":
            print("Try again, the field cannot be left blank")
            continue
        if not userInput.isdigit():
            print("Try again , the value you enter has to be a numerical character")
            continue
        
        room = int(userInput)

        if room < 1 or room > 12:
            print("Try again , the room number ranges from 1 - 12")
            continue
        else:
            break

    if rooms[room - 1] == "Booked":
        rooms[room - 1] = "Available"
        print("The booking for the hotel room as being sucessfully Cancelled")
    else:
        print("The room is already available")


#5.Check Room Status

def roomStatus(rooms):
    while True :
        userInput = input("Enter the room you want to cancel booking: ")
        if userInput == "":
            print("Try again, the field cannot be left blank")
            continue
        if not userInput.isdigit():
            print("Try again , the value you enter has to be a numerical character")
            continue
        
        room = int(userInput)

        if room < 1 or room > 12:
            print("Try again , the room number ranges from 1 - 12")
            continue
        else:
            break

    if rooms[room - 1] == "Available":
        print("The room is available")
    else:
        print("The room is booked")

#6.Show Statistics

def showStatistics(rooms):
    booked = "Booked"
    available = "Available"

    print("The total number of booked rooms:",rooms.count(booked))
    print("The total number of available rooms:",rooms.count(available))

#7.Menu system
def display(rooms):
    while True:
        print("----Ab4fulus Hotel Menu-----")
        print("1.View Rooms")
        print("2.Book Rooms")
        print("3.Cancel Booking")
        print("4.Check Room Status")
        print("5.Show Statistics")
        print("6.Exit")
        
        choice = input("Enter the option you picking: ")

        if choice == "1":
            displayRooms(rooms)
            continue
        elif choice == "2":
            bookRoom(rooms)
            continue
        elif choice == "3":
            cancelBooking(rooms)
            continue
        elif choice == "4":
            roomStatus(rooms)
            continue
        elif choice == "5":
            showStatistics(rooms)
            continue
        elif choice == "6":
            print("Have good day!")
            break
        else:
            print("Invalid choice")

def main():
    rooms = setUp()
    display(rooms)
    
main()
    
        
    
    

    


    
    
        
    
        
        
        
