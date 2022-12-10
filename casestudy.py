# Title         : Bowling Manager 2022 
# Purpose       : A bowling alley management program including inventory, active and archived games, and profits
#
# Programmers   : Amal,Athul,Danny,Minto 
# Date          : 3 DEC 2022
# Reference     :

#different options for selecting users need.
#Bowling score calculaor
#scores write in a file

import csv

# DW - Personal helper module to incorporate some of my most used functions
# Feel free to add more functions to the helper module but please comment and describe what it does
import dannyHelper as h 

# DW - Import the additional helper modules

import gameManager as gm
import settingsHelper as sh
import invHelper as ih

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
            loadSuccess = h.openFile('rb', True)
            if loadSuccess == "exit":
                return loadDefaultConfig()
            else:
                savedConfig = p.load(loadSuccess)
                loadSuccess.close()
                return savedConfig
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
        "Active":[],
        "Archived":[]
    }

    currentConfig = loadedConfig

    titleName = currentConfig["BusinessName"]

    inventory = []
    
    while True:
         #create menu options
        print(f"{titleName} - Main Menu\n{h.additionalSigns(f'{titleName} -Main Menu', True)}\n")       
        print(f"")
        print("You are at the main menu, please select an option from below:")
        print("1) View Active and Archived Bowling Games")
        print("2) Inventory")
        print("3) Check Today's Profits")
        print("4) Management Options")
        print("E) Exit")
        
        option = input("\nSelect an option: ").lower()
       
        if option == "1":
            gm.gamesMenu(bowlingGames, currentConfig)
        elif option == "2":
            ih.inventoryMenu(inventory)
        elif option == "3":
            checkProfits(bowlingGames, currentConfig)
        elif option == "4":
            sh.optionsMenu(currentConfig)
        elif option == "e":
            print("Exiting program...")
            break
       
        else:
            print("Please select a valid option")

def checkProfits():
    pass # DW - Placeholder for now

if __name__ == "__main__":
    main()
