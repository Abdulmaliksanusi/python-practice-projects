studentNames = ["ali","malik","sanusi","caleb","zion","drizzy","batman","gift","akshab"]
paymentAmounts = [0]*9

def displayStudentNamePaymentAmounts():
    for x in range(len(studentNames)):
        print("Student",x+1,"-",studentNames[x],"-",paymentAmounts[x])

def enterPayment():
    while True:
        userInput = input("Enter your student Number: ")
        if userInput == "":
            print("Try again , the field cannot be left blank!")
            continue
        if not userInput.isdigit():
            print("Try again , numerical characters only!")
            continue

        studentNumber = int(userInput)

        if studentNumber < 1 or studentNumber > 8:
            print("Try again , the student numbers range from 1 - 8")
            continue
        else:
            break

    while True:
        userInput = input("Enter the payment amount: ")
        if userInput == "":
            print("Try again, the field cannot be left blank")
            continue
        if not userInput.isdigit():
            print("Try again , numerical characters only!")
            continue

        paymentAmount = int(userInput)

        if paymentAmount < 0 or paymentAmount > 100:
            print("Try again , the payment amounts must be between 0 and 100")
            continue
        else:
            break

    paymentAmounts[studentNumber - 1] = paymentAmount
    print("Payment has been added sucessfully!")

def searchStudentName():
    found = False
    while True:
        userInput = input("Enter the name of the student you are looking for: ")
        if userInput == "":
            print("Try again , the field cannot be left blank")
            continue
        if not userInput.isalpha():
            print("Try again , letters only!")
            continue
        else:
            studentName = userInput.lower()
            break

    for x in range(len(studentNames)):
        if studentNames[x] == studentName:
            found = True
            print("The name has been found!")
    if not found:
        print("The name cannot be found!")

def searchPaymentAmounts():
    found = False
    while True:
        userInput = input("Enter the payment amount you are looking for: ")
        if userInput == "":
            print("Try again , the field cannot be left blank")
            continue
        if not userInput.isdigit():
            print("Try again , numerical characters only!")
            continue
        else:
            paymentAmount = int(userInput)
            break

    for x in range(len(paymentAmounts)):
        if paymentAmounts[x] == paymentAmount:
            found = True
            print("The payment amount has been found!")
    if not found:
        print("The payment amount cannot be found!")

def highestPayment():
    highest = paymentAmounts[0]
    index = 0
    for x in range(len(paymentAmounts)):
        if paymentAmounts[x] > highest:
            highest = paymentAmounts[x]
            index = x
    print("The highest payment:",highest)

def lowestPayment():
    lowest = paymentAmounts[0]
    index = 0
    for x in range(len(paymentAmounts)):
        if paymentAmounts[x] < lowest:
            lowest = paymentAmounts[x]
            index = x
    print("The lowest payment:",lowest)

def sortPayment():
    exchangemade = True
    while exchangemade == True:
        exchangemade = False
        for x in range(len(paymentAmounts)-1):
            if paymentAmounts[x] > paymentAmounts[x+1]:
                temp = paymentAmounts[x]
                paymentAmounts[x] = paymentAmounts[x+1]
                paymentAmounts[x+1] = temp
                exchangemade = True
    print("The payment amount in ascending order;",paymentAmounts)

def menuSystem():
    while True:
        print("-- School Trip Payment Tracker ---")
        print("1. View Students and Payments")
        print("2. Enter Payment")
        print("3. Search for Student Name")
        print("4. Search for Payment Amount")
        print("5. Show Highest and Lowest Payment")
        print("6. Sort Payments")
        print("7. Exit")

        choice = input("Enter the option you want: ")

        if choice == "1":
            displayStudentNamePaymentAmounts()
            continue
        elif choice == "2":
            enterPayment()
            continue
        elif choice == "3":
            searchStudentName()
            continue
        elif choice == "4":
            searchPaymentAmounts()
            continue
        elif choice == "5":
            highestPayment()
            lowestPayment()
            continue
        elif choice == "6":
            sortPayment()
            continue
        elif choice == "7":
            print("Have a good day!")
            break
        else:
            print("Invalid choice")

def main():
    menuSystem()
main()
    
            
        
