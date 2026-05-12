#1.Set up Attendance

def setUp():
    attendance = ["Absent"]* 8
    return attendance


def displayAttendance(attendance):
    for x in range(len(attendance)):
        print("Student",x+1,"-",attendance[x])

def markStudentPresent(attendance):
    while True:
        userInput = input("Enter your student number(1-8): ")
        if userInput == "":
            print("Try again , the field cannot be left blank")
            continue
        if not userInput.isdigit():
            print("Try again , only numeric characters allowed")
            continue
        studentNumber = int(userInput)

        if studentNumber < 1 or studentNumber > 8:
            print("Try again , the student number must be between 1 and 8")
            continue
        else:
            break

    if attendance[studentNumber - 1] == "Absent":
        attendance[studentNumber - 1] = "Present"
        print("The student has now being marked present")
    else:
        print("The student is already marked present")


def markStudentAbsent(attendance):
    while True:
        userInput = input("Enter your student number(1-8): ")
        if userInput == "":
            print("Try again , the field cannot be left blank")
            continue
        if not userInput.isdigit():
            print("Try again , only numeric characters allowed")
            continue
        studentNumber = int(userInput)

        if studentNumber < 1 or studentNumber > 8:
            print("Try again , the student number must be between 1 and 8")
            continue
        else:
            break

    if attendance[studentNumber - 1] == "Present":
        attendance[studentNumber - 1] = "Absent"
        print("The student has now being marked absent")
    else:
        print("The student is already marked absent")


def checkAttendance(attendance):
    while True:
        userInput = input("Enter your student number(1-8) you are seraching for: ")
        if userInput == "":
            print("Try again , the field cannot be left blank")
            continue
        if not userInput.isdigit():
            print("Try again , only numeric characters allowed")
            continue
        studentNumber = int(userInput)

        if studentNumber < 1 or studentNumber > 8:
            print("Try again , the student number must be between 1 and 8")
            continue
        else:
            break

    if attendance[studentNumber - 1] == "Absent":
        print("The student is absent")
    else:
        print("The student is present")

def showStatistics(attendance):
    present = "Present"
    absent = "Absent"

    print("Present:",attendance.count(present))
    print("Absent:",attendance.count(absent))

def findFirstAbsent(attendance):
   found = False
   for x in range(len(attendance)):
       if attendance[x] == "Absent":
           found = True
           print("The first absent student is", x + 1)
           break
   if not found:
       print("Everyone is present")

def menuSystem(attendance):
    while True:
        print("---Student Attendance Register---")
        print("1. View Attendance")
        print("2. Mark Present")
        print("3. Mark Absent")
        print("4. Check Attendance")
        print("5. Show Statistics")
        print("6. Find First Absent Student")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            displayAttendance(attendance)
            continue
        elif choice == "2":
            markStudentPresent(attendance)
            continue
        elif choice == "3":
            markStudentAbsent(attendance)
            continue
        elif choice == "4":
            checkAttendance(attendance)
            continue
        elif choice == "5":
            showStatistics(attendance)
            continue
        elif choice == "6":
            findFirstAbsent(attendance)
            continue
        elif choice == "7":
            print("Have a good day!")
            break
        else:
            print("Invalid choice")

def main():
    attendance = setUp()
    menuSystem(attendance)

main()
    



        


        
    
