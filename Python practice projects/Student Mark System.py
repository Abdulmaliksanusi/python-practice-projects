def setUp():
    revision = {
        "Ali" : 0,
        "Maya" : 0,
        "Noah" : 0,
        "Zara" : 0,
        "Leo" : 0
        }
    return revision

def DisplayStudents(revision):
    for student in revision:
        print(student ,"-", revision[student])

def addRevisionHours(revision):
    while True:
        userInput = input("Enter your student name: ")
        if userInput == "":
            print("Try again , the field cannot be left blank")
            continue
        if not userInput.isalpha():
            print("Try again , letters only!")
            continue

        studentName = userInput.capitalize()

        if studentName not in revision:
            print("Error , the name is invalid!")
            continue
        else:
            break

    while True :
        userInput = input("Enter the number of revision hours: ")
        if userInput == "":
            print("Try again , the field cannot be left blank")
            continue
        if not userInput.isdigit():
            print("Try again, numerical characters only!")
            continue

        revisionHour = int(userInput)

        if revisionHour < 0:
            print("The number you entered can't be less than 0")
            continue
        else:
            break

    revision[studentName] = revision[studentName] + revisionHour
    print("The revision hour has been added sucessfully!")

def removeRevisionHours(revision):
    while True:
        userInput = input("Enter your student name: ")
        if userInput == "":
            print("Try again , the field cannot be left blank")
            continue
        if not userInput.isalpha():
            print("Try again , letters only!")
            continue

        studentName = userInput.capitalize()

        if studentName not in revision:
            print("Error , the name is invalid!")
            continue
        else:
            break

    while True :
        userInput = input("Enter the number of revision hours: ")
        if userInput == "":
            print("Try again , the field cannot be left blank")
            continue
        if not userInput.isdigit():
            print("Try again, numerical characters only!")
            continue

        revisionHour = int(userInput)

        if revisionHour > revision[studentName]:
            print("The number you entered can't be less than the old value")
            continue
        else:
            break

    revision[studentName] = revision[studentName] - revisionHour
    print("The revision hour has been removed sucessfully!")

def checkStudentHours(revision):
    while True:
        userInput = input("Enter your student name: ")
        if userInput == "":
            print("Try again , the field cannot be left blank")
            continue
        if not userInput.isalpha():
            print("Try again , letters only!")
            continue

        studentName = userInput.capitalize()

        if studentName not in revision:
            print("Error , the name is invalid!")
            continue
        else:
            break

    print(studentName, "-" , revision[studentName])

def showStatistics(revision):
    total = sum(revision.values())
    highestRevisionHour = max(revision , key=revision.get)
    lowestRevisionHour = min(revision, key=revision.get)

    print("The student with the highest revision hours:", highestRevisionHour,"-",revision[highestRevisionHour])
    print("The student with the lowest revision hours:", lowestRevisionHour, "-", revision[lowestRevisionHour])
    print("The total revision hours completed by the class is:", total)

def menuSystem(revision):
    while True:
        print("------------------------------------------------------")
        print("------------------------MENU--------------------------")
        print("------------------------------------------------------")
        print("1.View Students")
        print("2.Add Revision Hours")
        print("3.Remove Revision Hours")
        print("4.Check Student Hours")
        print("5.Show Statistics")
        print("6.Exit")

        choice = input("Enter your number selection: ")

        if choice == "1":
            DisplayStudents(revision)
            continue
        elif choice == "2":
            addRevisionHours(revision)
            continue
        elif choice == "3":
            removeRevisionHours(revision)
            continue
        elif choice == "4":
            checkStudentHours(revision)
            continue
        elif choice == "5":
            showStatistics(revision)
            continue
        elif choice == "6":
            print("Have a good day!")
            break
        else:
            print("Invalid choice")

def main():
    revision = setUp()
    menuSystem(revision)

main()
    
    
    
    


    

