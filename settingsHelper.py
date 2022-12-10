# Title     :   settingsHelper
# Purpose   :   Assists with keeping track of settings and options for BowlingManager2022
#
# Programmer:   Athul,amal,danny and minto
# Date      :   December 7, 2022
# Reference :   

PROGRAM_NAME = "Bowling Manager 2022"

import dannyHelper as h
import casestudy as main

def optionsMenu(currentConfig): # DW - Put this menu in a loop
  changedConfig = currentConfig # DW - Store the currently running configuration in a temp var
  while True:
    h.titleMe("Management Options", False)
    print("Please select an option from below:")
    print("1) View/Change Business Name")
    print("2) View/Change Prices")
    print("3) View/Change Timezone Offset")
    print("4) View/Change Business Hours")
    print("5) View FAQs")
    print("6) Save Configuration")
    print("7) Load Configuration")
    print("8) Reset Configuration")
    print(f"9) About {PROGRAM_NAME}")
    print("V) View current running configuration")
    print("E) Return to main menu")

    choice = input("Enter your choice: ").lower()

    if choice == "1":
      changedConfig = change_location(changedConfig)
    elif choice == "2":
      changedConfig = change_price(changedConfig)
    elif choice == "3":
      changedConfig = change_timezone(changedConfig)
    elif choice == "4":
      changedConfig = changeBusinessHours(changedConfig)
    elif choice == "5":
      view_faqs()
    elif choice == "6":
      saveConfiguration(changedConfig)
    elif choice == "7":
      changedConfig = loadConfiguration(changedConfig)
    elif choice == "8":
      changedConfig = loadConfiguration("Default")
    elif choice == "9":
      view_about()
    elif choice == "v":
      viewRunningConfig(changedConfig)
    elif choice == "e":
      return changedConfig
    else:
      print("Invalid choice. Please try again.")

def viewRunningConfig(config):
  h.titleMe("View Running Configuration", False)
  print(f"Business Name:      {config['BusinessName']}")
  print(f"Price per Game:   $ {config['BaseGamePrice']:,.2f}")
  print(f"Price per Player: $ {config['PricePerPlayer']:,.2f}")
  print(f"Timezone Offset:    {config['TimeOffset']}")
  print("\nBusiness Hours:\n")
  for day, time in config["BusinessHours"].items():
    print(f"{day:<10} - {time}")
  input("\nPress ENTER to return to the menu...")

def changeBusinessHours(config):
  h.titleMe("View/Change Business Hours", False)
  for day, time in config["BusinessHours"].items():
    print(f"Current {day} business hours: {time}")
    changeInput = input("Please input new hours of operation (X:XX AM/PM - Y:YY AM/PM, blank to keep as-is)\nInput:   ").upper()
    if changeInput == (""):
      continue
    else:
      config["BusinessHours"][day] = changeInput
      print("Saved!")
  input("Press ENTER to return to the menu...")
  return config

def saveConfiguration(config):
  h.titleMe("Save Configuration", False)
  while True:
    userInput = input("Would you like to save your currently running configuration? (y/n):   ").lower()
    if userInput == "y":
      pickleResult = -1
      while pickleResult != 0:
          pickleResult = h.pickleFile(config)  # DW - Keep on attempting this command until success
      print("File saved!")
      input("Press ENTER to return to the main menu...")
      break
    elif userInput == "n":
      break

def loadConfiguration(originalConfig):
  h.titleMe("Load Configuration", False)
  while True:
    if not originalConfig == "Default":
      userInput = input("Would you like to load a saved configuration from a .dat file? (y/n):   ").lower()
      if userInput == "y":
          loadSuccess = h.openFile('rb', "File", True)
          if loadSuccess == "exit":
              return originalConfig
          elif loadSuccess == None:
              return originalConfig
          else:
              return loadSuccess
      elif userInput == "n":
          return originalConfig
    else:
      userInput = input("Would you like to reset your current configuration to default? (y/n):   ").lower()
      if userInput == "y":
          return main.loadDefaultConfig()
      elif userInput == "n":
          return originalConfig

def view_faqs():
  # FAQ for the bowling manager
  faq = {
      "How do I save a game in the app?": "To save a game in the app, go to the 'Games' tab and tap the 'Save' button. Enter a name for the game and tap 'Save' again.",
      "How do I change the settings in the app?": "To change the settings in the app, go to the 'Settings' tab and tap on the setting you want to change. Select the new value for the setting and tap 'Save' to apply the changes.",
      "Can I reset the settings to the default values?": "Yes, you can reset the settings to the default values by going to the 'Settings' tab and tapping the 'Reset configuration' button. This will restore all settings to their default values.",
  }

  # Print the FAQ
  print("FAQ:")
  for question, answer in faq.items():
    print(f"Q: {question}")
    print(f"A: {answer}")
    input("Press ENTER to continue...")

def change_location(config):
    h.titleMe("View/Change Business Name", False)
    # Print the user's current location
    print(f"Current Business Name: {config['BusinessName']}")

    # Ask the user for a new location
    new_location = input("Enter your new location (leave blank to exit): ")

    if new_location == "":  # DW - Make sure that they can keep the current name as-is
      return
    else:
      config["BusinessName"] = new_location

    # Print the user's new location
    print(f"Your new location is: {new_location}")
    input("Press ENTER to return to the menu...")
    return config

def change_timezone(config):
  # Ask the user for the new time zone
  print(config['TimeOffset'])
  print(f"Current Timezone Offset: {config['TimeOffset']}") # DW - Print out current time zone
  
  while True: # DW - Put this in a loop to verify input
    try:
      new_time_zone = input("Enter a new timezone offset (ex: For EST time, input -5. Leave blank to exit): ")
      # DW - Offer user a way to leave without changing the offset
      if new_time_zone == "":
        return config
      else:
        new_time_zone = float(new_time_zone)
        # Set the time zone of the system to the new time zone
        config["TimeOffset"] = new_time_zone

        # Print the new time zone
        print(f"Your new time zone is: {config['TimeOffset']}")
        input("Press ENTER to return to the menu...")
        return config
    except ValueError:
      print("That was not a valid input! Please try again...")


def view_about():
    # Information about the bowling manager
    about_text = """
    This is a bowling manager app that allows you to manage your bowling games,scores and user settings.

    Features:
    - Save and load games and scores
    - Keep track of business inventory and export it
    - Set custom settings for prices and business hours
    - Manage your bowling games easily and efficiently
    - And more!
    """

    # Print the information about the bowling manager
    print(about_text)
    input("Press ENTER to continue...")

def change_price(config):
  h.titleMe("View/Change Prices", False)
  # Prices per game and per player
  price_per_game = config["BaseGamePrice"]
  price_per_player = config["PricePerPlayer"]

  # DW - Print out current prices
  print(f"Current cost per game: ${price_per_game:,.2f}")

  # Ask the user for the new price per game
  while True:
    try:
      new_price_per_game = input("Enter the new price per game (leave blank to keep as-is): ")
      if new_price_per_game == "":
        break
      else:
        new_price_per_game = float(new_price_per_game)
        config["BaseGamePrice"] = new_price_per_game
        print("Saved!\n")
        break
    except ValueError:
      print("Please input a valid number!")
  
  print(f"Current cost per player: ${price_per_player:,.2f}")

  while True:
      try:
        new_price_per_player = input("Enter the new price per player (leave blank to keep as-is): ")
        if new_price_per_player == "":
          break
        else:
          new_price_per_player = float(new_price_per_player)
          config["PricePerPlayer"] = new_price_per_player
          print("Saved!\n")
          break
      except ValueError:
        print("Please input a valid number!")

  return config




    



    
