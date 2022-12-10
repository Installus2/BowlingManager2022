# Title     :   invHelper
# Purpose   :   Assists with keeping track of inventory for BowlingManager2022
#
# Programmer:   Athul ,minto,danny and amal
# Date      :   December 7, 2022
# Reference :   

PROGRAM_NAME = "Bowling Manager 2022"
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

# Function to add or update an item in the inventory
def add_or_update_inventory_item():
  # Prompt the user for the item and quantity
  item = input("Enter the item (blank to exit): ")

  # Continue prompting the user for items until they enter a blank space
  while item != "":
    quantity = int(input("Enter the quantity: "))

    # Add or update the item in the inventory
    inventory[item] = quantity

    # Prompt the user for the next item
    item = input("Enter the item (blank to exit): ")

# Test the add_or_update_inventory_item function
add_or_update_inventory_item()

# Write the updated inventory to the "inventory.txt" file
with open("inventory.txt", "w") as f:
  for item, quantity in inventory.items():
    f.write(f"{item}: {quantity}\n")

with open("inventory.txt", "r") as f:
  # Read the contents of the file into a list of strings
  lines = f.readlines()

# Print the contents of the file
print("\nInventory:")
for line in lines:
  print(line.strip())
# Print a success message
print("\nInventory successfully saved to inventory.txt.")
