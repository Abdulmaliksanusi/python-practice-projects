#1.Create dictionary

def createdictionary():
    snacks = {
        "Sandwich" : 0,
        "Water": 0,
        "Fruit": 0,
        "Juice": 0,
        "Biscuits": 0
        }
    return snacks

#2.Display all item names and their stock amounts

def displaySnacks(snacks):
    for product in snacks:
        print(product, "-", snacks[product])

#3.Add snacks

def addSnacks(snacks):
    while True:
        userInput = input("Enter the name of the product that you adding stock to: ")
        if userInput == "":
            print("Try again , the field canot be left blank")
            continue
        if not userInput.isalpha():
            print("Try again , enter only letters")
            continue

        itemName = userInput.capitalize()

        if itemName not in snacks:
            print("Invalid item, can not be found")
            continue
        else:
            break

    while True:
        userInput = input("Enter the amount of stock you want to add: ")
        if userInput == "":
            print("Try again , the field canot be left blank")
            continue
        if not userInput.isdigit():
            print("Try again , enter only numeric characters")
            continue

        valueAmount = int(userInput)

        if valueAmount < 0:
            print("Try again, amount cannot be negative")
            continue
        else:
            break

    snacks[itemName] =  snacks[itemName] + valueAmount
    print("The stock has been added sucessfully!")

#4.Remove snacks

def removeSnacks(snacks):
    while True:
        userInput = input("Enter the name of the product that you removing stock from: ")
        if userInput == "":
            print("Try again , the field canot be left blank")
            continue
        if not userInput.isalpha():
            print("Try again , enter only letters")
            continue

        itemName = userInput.capitalize()

        if itemName not in snacks:
            print("Invalid item, can not be found")
            continue
        else:
            break

    while True:
        userInput = input("Enter the amount of stock you are removing: ")
        if userInput == "":
            print("Try again , the field canot be left blank")
            continue
        if not userInput.isdigit():
            print("Try again , enter only numeric characters")
            continue

        valueAmount = int(userInput)

        if valueAmount > 0:
            print("Try again, amount cannot be negative")
            continue
        else:
            break

    snacks[itemName] = snacks[itemName] - valueAmount
    print("The stock has been removed sucessfully")

#5.Check snacks

def checkSnackStock(snacks):
    while True:
        userInput = input("Enter the name of the product that you are looking for: ")
        if userInput == "":
            print("Try again , the field canot be left blank")
            continue
        if not userInput.isalpha():
            print("Try again , enter only letters")
            continue

        itemName = userInput.capitalize()

        if itemName not in snacks:
            print("The product you are looking for can't be found")
            continue
        else:
            break

    print(itemName,"-",snacks[itemName])
    
    
#6.Show statistics

def showStatistics(snacks):
    totalSnacks = sum(snacks.values())
    highestSnacks = max(snacks, key=snacks.get)
    lowestSnacks = min(snacks, key=snacks.get)

    print("The total snacks of all items:",totalSnacks)
    print("The highest snack:",highestSnacks,"-",snacks[highestSnacks])
    print("The lowest snack:",lowestSnacks,"-",snacks[lowestSnacks])
          
#7.Menu System

def display(snacks):
    while True:
        print("---Ab4fulus School Canteen Stock System---")
        print("1.View snacks")
        print("2.Add snacks")
        print("3.Remove snacks")
        print("4.Check snacks")
        print("5.Show statistics")
        print("6.Exit")

        choice = input("Enter the option you wish to go with: ")

        if choice == "1":
            displaySnacks(snacks)
        elif choice == "2":
            addSnacks(snacks)
        elif choice == "3":
            removeSnacks(snacks)
        elif choice == "4":
            checkSnackStock(snacks)
        elif choice == "5":
            showStatistics(snacks)
        elif choice == "6":
            print("Have a good day!")
            break
        else:
            print("Try again, invalid choice")

def main():
    snacks = createdictionary()
    display(snacks)

main()
    
    

        
        
