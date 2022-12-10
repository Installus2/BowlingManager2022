# Title     :   invHelper
# Purpose   :   Assists with keeping track of inventory for BowlingManager2022
#
# Programmer:   Athul ,minto,danny and amal
# Date      :   December 7, 2022
# Reference :   

PROGRAM_NAME = "Bowling Manager 2022"

def inventoryMenu(): 
    # Inventory items and quantities
    inventory = {
        "balls": 30,
        "shoes": 60,
        "pins": 120,
        "towels": 50,
        "scorecards": 30,
        "food": 0,
        "drinks":0 ,
        "tables": 20,
        "chairs": 60,
        "ball-return machine":20
    }

    # Print the inventory items and quantities
    print("Inventory:")
    for item, quantity in inventory.items():
      print(f"{item}: {quantity}")
 
inventoryMenu()

    pass # DW - Placeholder for now
