# Title     :   settingsHelper
# Purpose   :   Assists with keeping track of settings and options for BowlingManager2022
#
# Programmer:   Athul,amal,danny and minto
# Date      :   December 7, 2022
# Reference :   

PROGRAM_NAME = "Bowling Manager 2022"

def optionsMenu(currentConfig):
  print("--- Bowling Alley Settings ---")
  print("1. view location")
  print("2. view price")
  print("3. View about information")
  print("4. view timezone")
  print("5. View FAQs")
  print("6. Exit")

  choice = input("Enter your choice: ")

  if choice == "1":
    change_location()
  elif choice == "2":
    change_price()
  elif choice == "3":
    view_about()
  elif choice == "4":
    change_timezone()
  elif choice == "5":
    view_faqs()
  elif choice == "6":
    return currentConfig
  else:
    print("Invalid choice. Please try again.")
    settings_menu()

  


def view_faqs():
  # FAQ for the bowling manager
  faq = {
      "How do I save a game in the app?": "To save a game in the app, go to the 'Games' tab and tap the 'Save' button. Enter a name for the game and tap 'Save' again.",
      "How do I change the settings in the app?": "To change the settings in the app, go to the 'Settings' tab and tap on the setting you want to change. Select the new value for the setting and tap 'Save' to apply the changes.",
      "Can I reset the settings to the default values?": "Yes, you can reset the settings to the default values by going to the 'Settings' tab and tapping the 'Reset configuration' button. This will restore all settings to their default values.",
      "How do I view statistics and graphs of my games?": "To view statistics and graphs of your games, go to the 'Statistics' tab. Here, you can see various graphs and statistics, such as your average score, highest score, and more."
  }

  # Print the FAQ
  print("FAQ:")
  for question, answer in faq.items():
    print(f"Q: {question}")
    print(f"A: {answer}")

def change_location():
    
    
    #get the users current location
    current_location = BuisnessName.get_location()

    # Print the user's current location
    print(f"Your current location is: {current_location}")

    # Ask the user for a new location
    new_location = input("Enter your new location: ")

    # Set the user's location to the new location
    BuisnessName.set_location(new_location)

    # Print the user's new location
    print(f"Your new location is: {new_location}")


def change_timezone():
        # Ask the user for the new time zone
    new_time_zone = input("Enter the new time zone: ")

    # Set the time zone of the system to the new time zone
    timezone = (filename).timezone(new_time_zone)

    # Print the new time zone
    print(f"Your new time zone is: {timezone}")

def view_about():
    # Information about the bowling manager
    about_text = """
    This is a bowling manager app that allows you to manage your bowling games,scores and user settings.

    Features:
    - Save and load games and scores
    - Set custom settings for price , user info,review games and start a new game etc...
    - Reset settings to defaults
    - View detailed statistics and graphs of your games and scores
    - And more!
    """

    # Print the information about the bowling manager
    print(about_text)

def change_price():
    # Prices per game and per player
    price_per_game = 10
    price_per_player = 5

    # Ask the user for the new price per game
    new_price_per_game = int(input("Enter the new price per game: "))

    # Update the price per game
    price_per_game = new_price_per_game

    # Ask the user for the new price per player
    new_price_per_player = int(input("Enter the new price per player: "))

    # Update the price per player
    price_per_player = new_price_per_player

    # Print the updated prices
    print(f"Price per game: {price_per_game}")
    print(f"Price per player: {price_per_player}")

options_menu()




    



    
