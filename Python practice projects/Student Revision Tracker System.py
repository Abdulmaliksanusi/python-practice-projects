def setUp():
    scores = [0] * 8
    return scores

def displayScores(scores):
    for x in range(len(scores)):
        print("Student",x+1,"-",scores[x])

def enterScore(scores):
    while True:
        userInput = input("Enter your student number: ")
        if userInput == "":
            print("Try again , the field cannot be left blank")
            continue
        if not userInput.isdigit():
            print("Try again , enter numerical characters only")
            continue

        studentNumber = int(userInput)

        if studentNumber < 1 or studentNumber > 8:
            print("Try again , the student number ranges from 1-8")
            continue
        else:
            break

    while True:
        userInput = input("Enter the score: ")
        if userInput == "":
            print("Try again , the field cannot be left blank")
            continue
        if not userInput.isdigit():
            print("Try again , enter numerical characters only")
            continue

        studentScore = int(userInput)

        if studentScore < 0 or studentScore > 100:
            print("Try again , the student scores must be between 0 and 100")
            continue
        else:
            break

    scores[studentNumber - 1] = studentScore
    print("Score has been added successfully")


def searchScore(scores):
    found = False
    while True:
        userInput = input("Enter the score: ")
        if userInput == "":
            print("Try again , the field cannot be left blank")
            continue
        if not userInput.isdigit():
            print("Try again , enter numerical characters only")
            continue

        studentScore = int(userInput)

        if studentScore < 0 or studentScore > 100:
            print("Try again , the student scores must be between 0 and 100")
            continue
        else:
            break

    for x in range(len(scores)):
        if score[x] == studentScore :
            found = True
            print("The score you are looking for has been found")
    if not found:
        print("The score cant be found")


def highestScore(scores):
    highest = scores[0]
    index = 0
    for x in range(len(scores)):
        if scores[x] > highest:
            highest = scores[x]
            index = x
    print("The highest score,", highest)

def lowestScore(scores):
    lowest = scores[0]
    index = 0
    for x in range(len(scores)):
        if scores[x] < lowest:
            lowest = scores[x]
            index = x
    print("The lowest score,",lowest)

def sortScores(scores):
    exchangemade = True
    while exchangemade == True:
        exchangemade = False
        for x in range(len(scores)-1):
            if scores[x] > scores[x+1]:
                temp = scores[x]
                scores[x] = scores[x+1]
                scores[x+1] = temp
                exchangemade = True
    print("The scores in ascending order;", scores)

def menuSystem(scores):
    while True:
        print("---AB4FULUS Test Score Search and Sort System---")
        print("1. View Scores")
        print("2. Enter Score")
        print("3. Search for Score")
        print("4. Show Highest and Lowest")
        print("5. Sort Scores")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            displayScores(scores)
            continue
        elif choice == "2":
            enterScore(scores)
            continue
        elif choice == "3":
            searchScore(scores)
            continue
        elif choice == "4":
            highestScore(scores)
            lowestScore(scores)
            continue
        elif choice == "5":
            sortScores(scores)
            continue
        elif choice == "6":
            print("Have a good day!")
            break
        else:
            print("Invalid choice")


def main():
    scores = setUp()
    menuSystem(scores)

main()
    
        
        
        
            
        
                
    

    
        


    
