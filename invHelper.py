# Title     :   invHelper
# Purpose   :   Assists with keeping track of inventory for BowlingManager2022
#
# Programmer:   Athul ,minto,danny and amal
# Date      :   December 7, 2022
# Reference :   

import dannyHelper as h
import pickle as p

PROGRAM_NAME = "Bowling Manager 2022"
# Inventory items and quantities

def inventoryMenu(inventory, currentConfig):
    while True:
        h.titleMe("Inventory", False)
        print("Please select an option from below: ")
        print("\n1) View inventory\n2) Add/Edit inventory\n3) Save inventory\n4) Load inventory\nE) Return to main menu")
        userInput = input("\nPlease select an option:   ").lower()
        if userInput == "e":
            break
        elif userInput == "1":
            viewInventory(inventory)
        elif userInput == "2":
            inventory = updateInventory(inventory)
        elif userInput == "3":
            saveInventory(inventory, currentConfig["TimeOffset"])
        elif userInput == "4":
            inventory = loadInventory(inventory)    # DW - Pass the original inventory in case user backs out
        else:
            print("Please make a valid selection!")

def viewInventory(inventory):   # DW - Added viewInventory function to view the inventory saved in memory
    h.titleMe("Add/Edit Inventory", False)
    print("Now printing current inventory:\n")
    grandTotal = 0
    for key, pair in inventory.items():
        print(f"{key+':':<20} x {pair[0]:<5} @ $ {pair[1]:,.2f}")
        grandTotal += pair[1] * pair[0]
    print(f"\nNet Value of Inventory: $ {grandTotal:,.2f}")
    input("Press ENTER to return to the menu...")

# Athul - Function to add or update an item in the inventory
def updateInventory(inventory):  # DW - Updated function name to shorten it down, modified function to suit the program

    h.titleMe("Add/Edit Inventory", False)
    print("Now printing current inventory:\n")
    for key, pair in inventory.items():
        print(f"{key+':':<20} x {pair[0]:<5} @ $ {pair[1]:,.2f}")

    # Athul - Continue prompting the user for items until they enter a blank space
    while True:

        # Athul - Prompt the user for the next item
        item = input("Enter the item you want to add/edit (blank to exit):   ").capitalize()
        if item == "":
            return inventory
        quantity = None
        while True:
            try:
                quantity = int(input("Enter the quantity:   "))
                if quantity < 0:
                    print("You cannot have negative inventory!")
                    continue
                elif quantity == 0:
                    while True:
                        deleteRequest = input("Would you like to delete this item from inventory? (y/n):   ").lower()
                        if deleteRequest == "y":
                            inventory.pop(item)
                            break
                        elif deleteRequest == "n":
                            break
                price = None

                if item not in inventory:
                    price = 10
                else:
                    price = inventory[item][1]
                
                while True:
                    newPrice = input(f"Enter the price per item (leave blank to keep price at $ {price:,.2f}):   ")
                    if newPrice == "":
                        break
                    else:
                        price = float(newPrice)
                    if price < 0:
                        print("You cannot have a negative price!")
                        continue
                    else:
                        break
                # Athul - Add or update the item in the inventory
                newArray = [quantity, price]
                inventory[item] = newArray
                break
            except ValueError:
                print("Please enter a valid input!")      

# Write the updated inventory to the "inventory.txt" file
def saveInventory(inventory, tzOffset):
    h.titleMe("Save Inventory", False)
    while True:
        saveAsTxt = input("Would you like to save the inventory as a .txt? (y/n, blank to exit):   ").lower()
        if saveAsTxt == "":
            break
        elif saveAsTxt == "y":
            fileToWrite = None
            while fileToWrite == None:
                fileToWrite = h.openFile('a', "File")
            if fileToWrite == "exit":
                break
            fileToWrite.write(h.fileTitle(fileToWrite.name.split(".txt")[0], tzOffset)+"\n")
            fileToWrite.write("\n")
            for key, pair in inventory.items():
                fileToWrite.write(f"{key+':':<20} x {pair[0]:<5} @ $ {pair[1]:,.2f}\n")
            fileToWrite.write("\n")
            fileToWrite.close()
            print("File saved!")
            input("Press ENTER to return to the main menu...")
            break

        elif saveAsTxt == "n":  # DW - Pickle the inventory for use for loading inventories
            pickleResult = -1
            while pickleResult != 0:
                pickleResult = h.pickleFile(inventory)  # DW - Keep on attempting this command until success
            print("File saved!")
            input("Press ENTER to return to the main menu...")
            break
        else:
            print("Please enter a valid selection!")

def loadInventory(ogInventory):
    h.titleMe("Load Inventory", False)
    while True:
        userInput = input("Would you like to load an inventory from a .dat file? (y/n):   ").lower()
        if userInput == "y":
            loadSuccess = h.openFile('rb', "File", True)
            if loadSuccess == "exit":
                return ogInventory
            elif loadSuccess == None:
                return ogInventory
            else:
                loadedInventory = p.load(loadSuccess)
                loadSuccess.close()
                return loadedInventory
        elif userInput == "n":
            return ogInventory
