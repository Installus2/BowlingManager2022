# Title         : Bowling Manager 2022 
# Purpose       : A bowling alley management program including inventory, active and archived games, and profits
#
# Programmers   : Amal,Athul,Danny,Minto 
# Date          : 3 DEC 2022
# Reference     :
#
# Inputs: Configuration file, inventory file, bowling game file
# Processing: Modifying configuration and inventory, switching bowling game status, changing scores of players
# Output: New configuration and inventory files (.txt and .dat), saved bowling game files (.txt and .dat)

#different options for selecting users need.
#scores write in a file

import csv

# DW - Personal helper module to incorporate some of my most used functions
# Feel free to add more functions to the helper module but please comment and describe what it does
import dannyHelper as h 

# DW - Import the additional helper modules

import gameManager as gm
import settingsHelper as sh
import invHelper as ih
import profitChecker as pc

import pickle as p

titleName = "Bowling Manager 2022"

def main():
   #    DW - Move main menu out of main()
    h.titleMe(titleName, True) # The second argument dictates if its the main title, if set to false it prints a less intricate title
    settingsConfig = loadConfigFile()
    mainMenu(settingsConfig)

def loadConfigFile():
    while True:
        askForSavedConfig = input("Would you like to load a previous saved config? (y/n):   ").lower()
        if askForSavedConfig == "y":
            loadSuccess = h.openFile('rb', True, True)
            if loadSuccess == "exit":
                return loadDefaultConfig()
            else:
                defaultConfig = loadDefaultConfig()
                for key in loadSuccess.keys():
                    if key not in defaultConfig:
                        print("This configuration appears to be incomplete! Using default config")
                        return loadDefaultConfig()
                return loadSuccess
        elif askForSavedConfig == "n":
            return loadDefaultConfig()
        else:
            print("Please make a valid selection!")
            

def loadDefaultConfig():
    bmSettings = {
        "PricePerPlayer":5,
        "BaseGamePrice":10,
        "BusinessName":"Danny's Alley",
        "TimeOffset":-5,
        "BusinessHours":{
            "Monday":"9:00 AM - 10:00 PM",
            "Tuesday":"9:00 AM - 10:00 PM",
            "Wednesday":"9:00 AM - 10:00 PM",
            "Thursday":"9:00 AM - 10:00 PM",
            "Friday":"9:00 AM - 10:00 PM",
            "Saturday":"9:00 AM - 10:00 PM",
            "Sunday":"9:00 AM - 10:00 PM"
        }
    }
    return bmSettings

def mainMenu(loadedConfig):
    global titleName

    bowlingGames = {
        "Active":{},
        "Archived":{}
    }

    currentConfig = loadedConfig

    titleName = currentConfig["BusinessName"]

    inventory = {
        "Bowling balls": [30, 50],  # DW - Inventory amount, price
        "Shoes": [60, 60],
        "Pins": [120, 20],
        "Towels": [50, 25],
        "Scorecards": [30, 1],
        "Food (tons)": [1, 200],
        "Drinks (litres)":[20, 25],
        "Tables": [20, 150],
        "Chairs": [60, 65],
        "Ball-return machine":[20, 500]
    }
    
    while True:
         #create menu options
        print(f"{titleName} - Main Menu\n{h.additionalSigns(f'{titleName} -Main Menu', True)}\n")       
        print("You are at the main menu, please select an option from below:")
        print("1) View Active and Archived Bowling Games")
        print("2) Inventory")
        print("3) Check Today's Profits")
        print("4) Management Options")
        print("E) Exit")
        
        option = input("\nSelect an option: ").lower()
       
        if option == "1":
            bowlingGames = gm.gamesMenu(bowlingGames, currentConfig)
        elif option == "2":
            ih.inventoryMenu(inventory, currentConfig)
        elif option == "3":
            pc.checkProfits(bowlingGames, currentConfig)
        elif option == "4":
            currentConfig = sh.optionsMenu(currentConfig)
        elif option == "e":
            print("Exiting program...")
            break
       
        else:
            print("Please select a valid option")

if __name__ == "__main__":
    main()
