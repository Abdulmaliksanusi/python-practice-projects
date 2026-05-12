import pandas as pd #This imports the panda as a variable "pd"
import matplotlib.pyplot as plt #This imports the matplotlib as a variable "plt"

#The csv file name is stored in the variable "dataFile"
datafile = "Task4b_data.csv" 

#This is are the columns that the program expects to find in the csv file 
requiredColumns = [ #This is the list of column names that the program expects to find in dataFile
    "Repair Type",
    "Region",
    "Number Of Devices",
    "Days To Complete"
    ]

#The role of the function is to load the data safely and make sure that the expected columns exist
def loadData():
    #Runs the code smoothly, if it's present and there's no errors associated with it
    try:
        records = pd.read_csv(dataFile) #This is opens and loads the data into the variable "records" which makes "records" the dataset
    
    #If the file is missing 
    except FileNotFoundError:
        print("Error: The file cannot be found !") #The program will display a file not found error message to the user 
        return None #There is no valid value to return as the file cannot be found

    #If there's any other errors that occurs during the reading of the file
    except Exception as error: #The variable "error" stores the error that may occur during the reading of the file
        print("Error reading file:",error) #This displays an error message to the user and the error that causes the problem
        return None
    
    
