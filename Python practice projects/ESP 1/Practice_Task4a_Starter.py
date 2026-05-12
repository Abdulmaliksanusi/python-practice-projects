import pandas as pd
import matplotlib.pyplot as plt

DataFile = "Practice_Task4a_data.csv"

RequiredColumns = [
    "Fault Type",
    "Store Region",
    "How Resolved",
    "Devices Affected",
    "Days To Resolve"
    ]

def loadData():
    try:
        faults = pd.read_csv(DataFile)

    except FileNotFoundError:
        print("Error: The file cannot be found!")
        return None

    except Exception as error:
        print("Error reading file:",error)
        return None

    for column in RequiredColumns:
        if column not in faults.columns:
            print("Error: Required column is missing:",column)
            return None

    faults["Days To Resolve"] = pd.to_numeric(
        faults["Days To Resolve"],errors = "coerce"
        )

    return faults

def displayTotalFaults(faults):
    total = faults["Fault Type"].value_counts()
    print("#############################################")
    print("#############Total Faults By type############")
    print("#############################################")
    print(total.to_string())

    total.plot(kind = "bar" , title = "Total Faults By Type")
    plt.xlabel("Fault Type")
    plt.ylabel("Number of Faults")
    plt.xticks(rotation = 45, ha= "right")
    plt.tight_layout()
    plt.show()

def displayAverageResolutionTime(faults):
    averageDays =(
        faults.groupby("Fault Type")["Days To Resolve"]
        .mean()
        .round(2)
        .sort_values(ascending=False)
        )
    print("#############################################")
    print("#############Average Resolution Time By Type############")
    print("#############################################")
    print(averageDays.to_string())

    averageDays.plot(kind = "bar", title = "Average Resolution Time By Type")
    plt.xlabel("Fault Type")
    plt.ylabel("Average Days To Resolve")
    plt.xticks(rotation = 45, ha = "right")
    plt.tight_layout()
    plt.show()

def displayFaultsByStoreRegion(faults):
    faultsByRegion = pd.crosstab(faults["Store Region"],faults["Fault Type"])
    print("#############################################")
    print("#############Faults By Store Region############")
    print("#############################################")
    print(faultsByRegion.to_string())

    faultsByRegion.plot(kind = "bar",stacked = True, title = "Faults by Store Region")
    plt.xlabel("Store region")
    plt.ylabel("Number of faults")
    plt.xticks(rotation = 45, ha = "right")
    plt.tight_layout()
    plt.show()

def displayResolutionsByStoreRegion(faults):
    ResolutionsByStoreRegion = pd.crosstab(faults["Store Region"],faults["How Resolved"])
    print("#############################################")
    print("#############Resolutions By Store Region############")
    print("#############################################")
    print(ResolutionsByStoreRegion.to_string())

    faultsByRegion.plot(kind = "bar",stacked = True, title = "Resolutions by Store Region")
    plt.xlabel("Store region")
    plt.ylabel("Number of Resolutions")
    plt.xticks(rotation = 45, ha = "right")
    plt.tight_layout()
    plt.show()

def menu(faults):
    while True:
        print("\n####################################################")
        print("############# Nexa Mobile Repairs System #############")
        print("####################################################")
        print("1.Total Faults By type")
        print("2.Average Resolution Time By Type")
        print("3.Faults By Store Region")
        print("4.Resolutions By Store Region")
        print("5. Exit")
        
        choice = input("Enter your number selection here: ")
        
        if choice == "1":#if the user chooses 1
            displayTotalFaults(faults) #calls the function and displays total issues
            continue
        elif choice == "2":#if the user enters 2
            displayAverageResolutionTime(faults)#calls the function and displays average resolution time
            continue
        elif choice == "3":#if the user chooses 3 
            displayFaultsByStoreRegion(faults)#calls the function and displays issues by region
            continue
        elif choice == "4":#if the user chooses 4
            displayResolutionsByStoreRegion(faults) #calls the function and displays resolutions by region
            continue
        elif choice == "5":#if the user chooses 5
            print("Have a good day!")#Displays the message to the user
            break#ends the program
        else:
            print("Invalid choice")# if the number selection is below 1 or above 5 , the program displays a error message to the user
    
def main():
    faults = loadData()
    if faults is None:#Data fails to load
        return#stops and exit the program , if the data failed to load 
    menu(faults)
main()


    

    
    
    
