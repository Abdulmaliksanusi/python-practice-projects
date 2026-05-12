def setUp():
    uniform = {
        "Blazer" : 0,
        "Tie" : 0,
        "Shirt" : 0,
        "jumper" : 0,
        "Trousers" : 0
        }
    return uniform

def displayUniform(uniform):
    for product in uniform:
        print(product,"-",uniform[product])

def addStock(uniform):
    while True:
        userInput = input("Enter the item name: ")
        if userInput == "":
            print("Try again , the field cannot be left blank")
            continue
        if not userInput.isalpha():
            print("Try again , letters only")
            continue

        itemName = userInput.capitalize()

        if itemName not in uniform:
            print("The item can not be found!")
            continue
        else:
            break

    while True:
        userInput = input("Enter the amount of stock you are adding: ")
        if userInput == "":
            print("Try again , the field cannot be left blank")
            continue
        if not userInput.isdigit():
            print("Try again , numerical characters only")
            continue

        valueAmount = int(userInput)

        if valueAmount < 0:
            print("The stock you are adding cannot be below 0")
            continue
        else:
            break

    uniform[itemName] =  uniform[itemName] + valueAmount
    print("The stock has been added sucessfully")

def removeStock(uniform):
    while True:
        userInput = input("Enter the item name: ")
        if userInput == "":
            print("Try again , the field cannot be left blank")
            continue
        if not userInput.isalpha():
            print("Try again , letters only")
            continue

        itemName = userInput.capitalize()

        if itemName not in uniform:
            print("The item can not be found!")
            continue
        else:
            break

    while True:
        userInput = input("Enter the amount of stock you are removing: ")
        if userInput == "":
            print("Try again , the field cannot be left blank")
            continue
        if not userInput.isdigit():
            print("Try again , numerical characters only")
            continue

        valueAmount = int(userInput)

        if valueAmount > uniform[itemName]:
            print("The stock you are removing cannot be higher than the old stock value")
            continue
        else:
            break

    uniform[itemName] =  uniform[itemName] - valueAmount
    print("The stock has been removed sucessfully")
    
def checkStock(uniform):
    while True:
        userInput = input("Enter the item name you are looking for: ")
        if userInput == "":
            print("Try again , the field cannot be left blank")
            continue
        if not userInput.isalpha():
            print("Try again , letters only")
            continue

        itemName = userInput.capitalize()

        if itemName not in uniform:
            print("The item can not be found!")
            continue
        else:
            break

    print(itemName,"-",uniform[itemName])

def showStatistics(uniform):
    totalStock = sum(uniform.values())
    highestStock = max(uniform , key=uniform.get)
    lowestStock = min(uniform , key=uniform.get)

    print("The total stock of all items combined:",totalStock)
    print("The item with the highest stock:",highestStock,"-",uniform[highestStock])
    print("The item with the lowest stock:",lowestStock,"-",uniform[lowestStock])

def menuSystem(uniform):
    while True:
        print("--- School Uniform Stock System ---")
        print("1. View Uniform")
        print("2. Add Stock")
        print("3. Remove Stock")
        print("4. Check Stock")
        print("5. Show Statistics")
        print("6. Exit")

        choice = input("Enter the option you want: ")

        if choice == "1":
            displayUniform(uniform)
            continue
        elif choice == "2":
            addStock(uniform)
            continue
        elif choice == "3":
            removeStock(uniform)
            continue
        elif choice == "4":
            checkStock(uniform)
            continue
        elif choice == "5":
            showStatistics(uniform)
            continue
        elif choice == "6":
            print("Have a good day!")
            break
        else:
            print("Invalid choice")

def main():
    uniform = setUp()
    menuSystem(uniform)
main()
    
    
    
