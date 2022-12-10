# Title     :   gamaManager
# Purpose   :   Assists with keeping track of games for BowlingManager2022
#
# Programmer:   Danny, Minto, Athul, and Amal
# Date      :   December 7, 2022
# Reference :   

import dannyHelper as h

PROGRAM_NAME = "Bowling Manager 2022"

def gamesMenu(bowlingGames, bmSettings):
   while True:
    print(f"\n{h.titleMe('Games Menu', False)}")
    print("Please make a selection from the options below:")
    print("1) View current active games")
    print("2) Add new game")
    print("3) Archive all current games")
    print("4) View archived games")
    print("E) Return to main menu")

    choice = input("Select an option: ").lower()
    
    if choice == "1":
        bowlingGames = activeList(bowlingGames)
        
    elif choice == "2":
        newGame = addGame(bmSettings["TimeOffset"])
        bowlingGames["Active"].append(newGame)
        
    elif choice == "3":
        archiveGame("All")
        
    elif choice == "e":
        break
        
    else:
        print("That was not a valid option! Please try again.")

def activeList(activeGames):
    h.titleMe("Active Games List", False)
    activeList = activeGames["Active"]
    selectedGame = None
    for i in range(0, len(activeGames["Active"])):
        print(f"{i+1}) ")

def defaultGameListing():
    gameListing = {
        "DateTimeGenerated":[],
        "Players":[],
        "GameType":"10-Pin"
    }
    return gameListing
      
#for starting a new bowling game        
def addGame(timeOffset):
    h.titleMe(PROGRAM_NAME, False)
    amountOfPlayers = None
    gameType = None
    newListing = defaultGameListing()
    
    while True:
        try:
            amountOfPlayers = int(input("How many players are playing in this game?:   "))
            break
        except ValueError:
            print("That was not a valid input, please try again!")
        except EOFError:
            print("That was not a valid input, please try again!")

    for i in range(0, amountOfPlayers):
        newPlayer = {
            "Name":"None",
            "Score":0
        }
        nameInput = input(f"Please enter the name of player #{i+1}: ")
    
    while True:
        try:
            gameType = input("How many pins are used in this game? (leave blank for 10-pin):   ")
            if gameType == "":
                gameType = 10
            else:
                gameType = int(gameType)
            break
        except ValueError:
            print("That was not a valid input, please try again!")
        except EOFError:
            print("That was not a valid input, please try again!")
    
    newListing["GameType"] = str(gameType)+"-pin"

    genTime = h.timeMe(timeOffset)
    newListing["DateTimeGenerated"] = [genTime[0], genTime[1]]

    return newListing

#bowling histories
def archiveGame():
    print("Archive all current games")