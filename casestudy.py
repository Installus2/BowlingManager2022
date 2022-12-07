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

PROGRAM_NAME = "Bowling Manager 2022"

def main():
   #    DW - Move main menu out of main()
    h.titleMe(PROGRAM_NAME, True) # The second argument dictates if its the main title, if set to false it prints a less intricate title
    mainMenu()

def mainMenu():
    
    while True:
         #create menu options
        print(f"Main Menu\n{h.additionalSigns('Main Menu', True)}\n")       
        print("You are at the main menu, please select an option from below:")
        print("1) View active and archived bowling games")
        print("2) Inventory")
        print("3) Check today's profits")
        print("4) Management options")
        print("E) Exit")
        
        option = input("\nSelect an option: ").lower()
       
        if option == "1":
            gm.gamesMenu()
        elif option == "2":
            inventoryMenu()
        elif option == "3":
            checkProfits()
        elif option == "4":
            optionsMenu()
        elif option == "e":
            print("Exiting program.....")
            break
       
        else:
            print("Please select a valid option")

def checkProfits():
    pass # DW - Placeholder for now

def optionsMenu():
    pass # DW - Placeholder for now

def inventoryMenu():
    pass # DW - Placeholder for now

if __name__ == "__main__":
    main()
