# Create list of 10 seats (all start as Available)
seats = ["Available"] * 10


# 1. View Seats
def viewSeats():
    print("\n--- SEAT STATUS ---")
    for i in range(10):
        print(f"Seat {i+1} - {seats[i]}")


# 2. Book Seat
def bookSeat():
    while True:
        userInput = input("Enter seat number (1-10): ")

        if userInput == "":
            print("Cannot be empty. Try again.")
            continue

        if not userInput.isdigit():
            print("Must be a number.")
            continue

        seat = int(userInput)

        if seat < 1 or seat > 10:
            print("Seat must be between 1 and 10.")
            continue

        break

    if seats[seat - 1] == "Available":
        seats[seat - 1] = "Booked"
        print("Seat successfully booked!")
    else:
        print("That seat is already booked.")


# 3. Cancel Booking
def cancelBooking():
    while True:
        userInput = input("Enter seat number to cancel (1-10): ")

        if userInput == "":
            print("Cannot be empty. Try again.")
            continue

        if not userInput.isdigit():
            print("Must be a number.")
            continue

        seat = int(userInput)

        if seat < 1 or seat > 10:
            print("Seat must be between 1 and 10.")
            continue

        break

    if seats[seat - 1] == "Booked":
        seats[seat - 1] = "Available"
        print("Booking cancelled.")
    else:
        print("That seat is already available.")


# 4. Check Seat Status
def checkSeat():
    seat = int(input("Enter seat number (1-10): "))

    if seats[seat - 1] == "Available":
        print("Seat is Available")
    else:
        print("Seat is Booked")


# 5. Show Statistics
def showStats():
    booked = seats.count("Booked")
    available = seats.count("Available")

    print(f"Booked seats: {booked}")
    print(f"Available seats: {available}")


# 6. Menu System
def main():
    while True:
        print("\n--- CINEMA MENU ---")
        print("1. View Seats")
        print("2. Book Seat")
        print("3. Cancel Booking")
        print("4. Check Seat")
        print("5. Show Statistics")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            viewSeats()
        elif choice == "2":
            bookSeat()
        elif choice == "3":
            cancelBooking()
        elif choice == "4":
            checkSeat()
        elif choice == "5":
            showStats()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


# Run program
main()
