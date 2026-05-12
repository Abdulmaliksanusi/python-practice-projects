#1.Set Up Marks

def setUp():
    marks = [0] * 10
    return marks

#2.Display Marks

def displayMark(marks):
    for i in range(len(marks)):
        print("Student",i+1, "-", marks[i])

#3.Enter a Mark

def enterMark(marks):
    while True:
        userInput = input("Enter your student number: ")
        if userInput == "":
            print("Try again , the field cannot be left blank")
            continue
        if not userInput.isdigit():
            print("Try again , the value you enter has to be a numeric character")
            continue
        
        studentNumber = int(userInput)

        if studentNumber < 1 or studentNumber >10:
            print("Try again , the number ranges from 1-10")
            continue
        else:
            break

    while True:
        userInput = input("Enter the mark you got: ")
        if userInput == "":
            print("Try again , the field cannot be left blank")
            continue
        if not userInput.isdigit():
            print("Try again , the value you enter has to be a numeric character")
            continue
        
        mark = int(userInput)

        if mark  < 0 or mark >100:
            print("Try again , the number ranges from 0-100")
            continue
        else:
            print("The mark has been added sucesfully")
            break


    marks[studentNumber - 1 ] = mark

    

#4. Search for a mark

def searchMark(marks):
    found = False
    while True:
        userInput = input("Enter the mark you are searching for: ")
        if userInput == "":
            print("Try again , the field cannot be left blank")
            continue
        if not userInput.isdigit():
            print("Try again , the value you entered has to be a numerical character")
            continue
        else:
            markBeingSearched = int(userInput)
            break
        
    for x in range(len(marks)):
        if markBeingSearched == marks[x]:
            found = True
            
    if found:
        print("The mark you are searching for has been found in the list containing the marks")
    else:
        print("The mark doesn't exist in the list")
        

def highestMark(marks):
    biggest = marks[0]
    for x in range(len(marks)):
        if marks[x] > biggest:
            biggest = marks[x]
    print("The highest mark is ", biggest)


def lowestMark(marks):
    smallest = marks[0]
    for x in range(len(marks)):
        if marks[x] < smallest:
            smallest = marks[x]
    print("The lowest mark is ", smallest)

def sortMarks(marks):
    exchangemade = True
    while exchangemade == True:
        exchangemade = False
        for x in range(len(marks)-1):
            if marks[x] > marks[x+1]:
                temp = marks[x]
                marks[x] = marks[x+1]
                marks[x+1] = temp
                exchangemade = True
    print("The marks in ascending order",marks)

def display(marks):
    while True:
        print("---ab4fulus student mark system---")
        print("1.View Marks")
        print("2.Enter Mark")
        print("3.Search for Mark")
        print("4.Show Highest and Lowest")
        print("5.Sort Marks")
        print("6.Exit")

        choice = input("Enter the option you wish to use: ")

        if choice == "1":
            displayMark(marks)
            continue
        elif choice == "2":
            enterMark(marks)
            continue
        elif choice == "3":
            searchMark(marks)
            continue
        elif choice == "4":
            highestMark(marks)
            lowestMark(marks)
            continue
        elif choice == "5":
            sortMarks(marks)
            continue
        elif choice == "6":
            print("Have a good day!")
            break
        else:
            print("Try again , invalid choice")

def main():
    marks = setUp()
    display(marks)

main()
            
            
            
            
        
        


        

        
        
            
