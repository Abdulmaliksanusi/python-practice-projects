#1.Set Up Stock

def setUp():
    stocks = {
        "Bread": 0,
        "Milk": 0,
        "Eggs": 0,
        "Juice": 0,
        "Crisps": 0
    }
    return stocks


#2.Display Products

def displayProducts(stocks):
    for product in stocks:
        print(product, "-", stocks[product])


#3.Add Stock

def addStock(stocks):
    while True:
        userInput = input("Enter the product name: ")
        if userInput == "":
            print("Try again, the field cannot be left blank")
            continue
        if not userInput.isalpha():
            print("Try again, it has to be letters")
            continue

        product = userInput.capitalize()

        if product not in stocks:
            print("Try again, that product does not exist")
            continue
        else:
            break

    while True:
        userInput = input("Enter the amount of stock you want to add: ")
        if userInput == "":
            print("Try again, the field cannot be left blank")
            continue
        if not userInput.isdigit():
            print("Try again, it has to be numeric characters")
            continue

        amount = int(userInput)

        if amount < 0:
            print("Try again, amount cannot be negative")
            continue
        else:
            break

    stocks[product] = stocks[product] + amount
    print("Stock added successfully")


#4.Remove Stock

def removeStock(stocks):
    while True:
        userInput = input("Enter the product name: ")
        if userInput == "":
            print("Try again, the field cannot be left blank")
            continue
        if not userInput.isalpha():
            print("Try again, it has to be letters")
            continue

        product = userInput.capitalize()

        if product not in stocks:
            print("Try again, that product does not exist")
            continue
        else:
            break

    while True:
        userInput = input("Enter the amount of stock you want to remove: ")
        if userInput == "":
            print("Try again, the field cannot be left blank")
            continue
        if not userInput.isdigit():
            print("Try again, it has to be numeric characters")
            continue

        amount = int(userInput)

        if amount < 0:
            print("Try again, amount cannot be negative")
            continue
        else:
            break

    if amount > stocks[product]:
        print("You cannot remove more stock than the product currently has")
    else:
        stocks[product] = stocks[product] - amount
        print("Stock removed successfully")


#5.Check Stock

def checkStock(stocks):
    while True:
        userInput = input("Enter the product name: ")
        if userInput == "":
            print("Try again, the field cannot be left blank")
            continue
        if not userInput.isalpha():
            print("Try again, it has to be letters")
            continue

        product = userInput.capitalize()

        if product not in stocks:
            print("Try again, that product does not exist")
            continue
        else:
            break

    print(product, "-", stocks[product])


#6.Show Statistics

def showStatistics(stocks):
    totalStock = 0
    highestProduct = ""
    lowestProduct = ""

    firstProduct = True

    for product in stocks:
        totalStock = totalStock + stocks[product]

        if firstProduct == True:
            highestProduct = product
            lowestProduct = product
            firstProduct = False
        else:
            if stocks[product] > stocks[highestProduct]:
                highestProduct = product
            if stocks[product] < stocks[lowestProduct]:
                lowestProduct = product

    print("Total stock of all products:", totalStock)
    print("Product with the highest stock:", highestProduct, "-", stocks[highestProduct])
    print("Product with the lowest stock:", lowestProduct, "-", stocks[lowestProduct])


#7.Menu System

def display(stocks):
    while True:
        print("\n--- Mini Shop Stock System ---")
        print("1. View Products")
        print("2. Add Stock")
        print("3. Remove Stock")
        print("4. Check Stock")
        print("5. Show Statistics")
        print("6. Exit")

        choice = input("Enter the option you wish to use: ")

        if choice == "1":
            displayProducts(stocks)
        elif choice == "2":
            addStock(stocks)
        elif choice == "3":
            removeStock(stocks)
        elif choice == "4":
            checkStock(stocks)
        elif choice == "5":
            showStatistics(stocks)
        elif choice == "6":
            print("Have a good day!")
            break
        else:
            print("Try again, invalid choice")


#Main Procedure

def main():
    stocks = setUp()
    display(stocks)

main()
