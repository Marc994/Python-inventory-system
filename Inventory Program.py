
import datetime #Import the datetime module to get current date and time for reports

inventory = { #Dictionary of store inventory items defined with name, quantity, price and ID
    1: {"Name": "Hammer", "Quantity": 15, "Price": 26.55},#Item ID 1, Hammer    
    2: {"Name": "Saw", "Quantity": 10, "Price": 13.25}, #Item ID 2, Saw
    3: {"Name": "Nails", "Quantity": 250, "Price": 1}, #Item ID 3, Nails
    4: {"Name": "Saw Blades", "Quantity": 5, "Price": 5.50} #Item ID 4, Saw Blades
} #Dictionary closed


def viewItems():#Function defined to view all items in inventory
    if not inventory:#Check if inventory dictionary is empty
        print("No items in Inventory")#message printed if inventory is empty
    else: #final catch all else statement if inventory is not empty
        for itemID, details in inventory.items():#Loop through each item in inventory dictionary
            print(f"Item ID: {itemID}, Name: {details['Name']}, Quantity: {details['Quantity']}, Price: {details['Price']}")
            #Items printed using formatted string 

def addItem():#Function defined to view all items in inventory 
    try: #Try and except error handling 
        itemID = int(input("Enter new item ID: ")) #Prompt user to enter item ID and convert to integer
        if itemID in inventory: #Check if item ID already exists in inventory
                print("Item already exists in inventory.") #Print message if item already exists
                return #Return function to exit the function early
        name = input("Enter item name: ") #Prompt user to enter item name
        quantity = int(input("Enter amount: ")) #Prompt user to enter quantity and convert to integer
        price = float(input("Enter price per item: ")) #Prompt user to enter price and convert to float
        inventory[itemID] = {"Name" : name,"Quantity" : quantity,"Price" : price} #Add new item to inventory
        print("Item Added") #Message printed to screen confirming item added
    except ValueError: #Except handling if input conversion fails
        print("Invalid input, please enter valid unit type. ") #Error message printed to screen
        

def updateItem(): #Function defined to update existing item iun inventory
    try:
        itemID = int(input("Enter item ID you wish to update: "))  #Prompt user for items ID to update
        if itemID in inventory: #Check if item ID exists in inventory
            name = input("Enter new name: ") #Prompt user for new name
            quantity = int(input("Enter new quantity: ")) #prompt user for quantity of updated item and converted to Integer
            price = float(input("Enter new price per unit: ")) #Prompt user for price per unit of updated item and converted to float
            inventory[itemID] = {"Name": name, "Quantity": quantity, "Price": price} #Line to update item in inventory
            print("Item updated successfully") #confirmation message that item has been successfully updated
        else:
            print("Item not found.") #Error message printed if item ID not found
    except ValueError: #Except value error for invalid input
        print("Invalid input, please enter valid unit type. ") #error message printed to screen for invalid input
        

def deleteItem(): #Function defined to delete existing item from inventory
    try: #Try except handling
        itemID = int(input("Enter item ID you wish to delete: ")) #Prompt user for item ID to delete
        if itemID not in inventory: #Check if item ID is not in inventory
                     print("That item ID does not exist in register, please enter valid item ID. ") #Error message printed to screen
        else:
            del inventory[itemID] #del function to delete function from inventory
        print("Item successfully deleted. ") #Confirmation message if item deleted succesfully
    except ValueError:#Except value error for invalid input
        print("Invalid input, please enter valid unit type. ") #error message printed to screen for invalid input
        

def generateReport(): #Function defined to generate a report for all items in inventory
    totalItems = sum(item['Quantity'] for item in inventory.values()) #Calculate total quantity of all items
    totalValue = sum(item['Quantity'] * item['Price']for item in inventory.values()) #Calculate total inventory value (Total cost)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") #Timestamp module as previously imported to handle report date/time

    report= [ #List created with variable value 'report'
        "Inventory report;",#Report Title
        f"Timestamp: {timestamp}", #Current timestampt added to report file
        f"Total Inventoryt value: ${totalValue}", #Total value of all inventory items added to report
        f"Total number of items: {totalItems}", #Total number of items added to report
        "Item List:" #Section heading for item list
    ]#Report list closed
    for itemID, item in inventory.items(): #Loop through all items in inventory
        report.append(f"ID: {itemID}, Name: {item['Name']}, Quantity: {item['Quantity']}, Price: ${item['Price']}")#F function and append function to write report as a string to report list

    filename = "InventoryReport.txt" #File name set for report
    with open(filename, 'w') as file: #W used to opens file in 'write' mode
        for line in report: #loop through each line in report list
            print(line) #Prints line to screen
            file.write(line + "\n") #Writes each line to file with newline character (found in reference list)

    print(f"\nInventory report written to {filename}.") #Message confirming report was saved




def menu(): #Function defined creating a Menu for user to interact with
    print("Hardware Inventory program Menu") #Menu title printed to screen
    while True: #Infinite loop to keep showing menu title to user until option 6 (Exit) is chosen
            print("\n1. View inventory. ") #Option 1, View inventory, printed to new line
            print("2. Add item. ") #Option 2, Add Item, printed to screen
            print("3. Update existing item. ") #Option 3 printed to screen
            print("4. Delete Item. ") #Option 4 printed to screen
            print("5. Create inventory report. ") #Option 5 printed to screen
            print("6. Exit program. \n") #Option 6, Exit program,  printed to screen

            choice = input("Please select an option: ") #Prompt user to choose menu option

            if choice == "1": #If statement for option 1
                viewItems()#Calls viewItem function
            elif choice == "2": #elif statement for option 2
                addItem() #Calls addItem Function
            elif choice == "3":#elif statement for option 3
                updateItem()#Calls updateItem function
            elif choice == "4":#elif statement for option 4
                deleteItem()#Calls deletItem function
            elif choice == "5":#elif statement for option 5
                generateReport()#Calls GenerateReport function
            elif choice == "6":#elif statement for option 6
                print("Exiting Hardware Inventory program, have a nice day!") #Exit message 
                break #Exit while loop and end the program
            else: #Else statement for invalid input
                print("Invalid choice, please enter an option from 1 to 6") #Invalid input error message

menu() #Call the menu function to start the program

        
        



