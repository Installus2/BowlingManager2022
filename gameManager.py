# Title     :   gamaManager
# Purpose   :   Assists with keeping track of games for BowlingManager2022
#
# Programmer:   Danny, Minto, Athul, and Amal
# Date      :   December 7, 2022
# Reference :   

import dannyHelper as h

PROGRAM_NAME = "Bowling Manager 2022"

bowlingList = None
activeSettings = None

def gamesMenu(bowlingGames, bmSettings):
    global bowlingList
    global activeSettings

    bowlingList = bowlingGames
    activeSettings = bmSettings

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
            printGameList("Active")
        elif choice == "2":
            newGame = addGame(activeSettings["TimeOffset"])
            bowlingGames["Active"].append(newGame)
        elif choice == "3":
            archiveGame("All")
        elif choice == "4":
            printGameList("Archived")
        elif choice == "e":
            break    
        else:
            print("That was not a valid option! Please try again.")

def printGameList(gameStatus):
    while True:
        h.titleMe("Active Games List", False)
        gamesList = bowlingList[gameStatus]
        selectedGame = None
        for i in range(0, len(gamesList)):
            print(f"{i+1}) {len(gamesList[i]['Players'] / 2)}-player game @ {gamesList[i]['DateTimeGenerated'][1]}")
        selectedGame = input("\nPlease select a game you wish to view (blank to return to menu):   ")
        if selectedGame == "":
            break
        else:
            try:
                selectedGame = int(selectedGame) - 1
                changeStatus = viewListing(gamesList[selectedGame], gameStatus)
            except ValueError:
                print("That was not a valid input, please try again!")
            except EOFError:
                print("That was not a valid input, please try again!")
            finally:
                input("Press ENTER to return to the game list...")

def viewListing(selectedGame, gameStatus):
    while True:
        h.titleMe("View Listing", False)

        print(f"Generation Time/Date: {selectedGame['DateTimeGenerated'][0]} - {selectedGame['DateTimeGenerated'][1]}")
        print(f"Game status: {gameStatus}")

        if gameStatus == "Archived":
            print(f"Archive time: {selectedGame['ArchivedAt'][0]} - {selectedGame['ArchivedAt'][1]}")

        print(f"Players:\n")
        for i in range(0, len(selectedGame['Players']/2)):
            print(f"Player {(i+1)+'.':<5} {selectedGame['Players']['Name']:<15} | Score: {selectedGame['Players']['Score']}")

        print("\nYou can make the following options"+
        f"\n1) Edit the score of a player\n2) {archiveOrActivate(gameStatus)} this game\nR) Return to the game list")

        userInput = input("\nPlease make a selection:   ").lower()
        if userInput == "r":
            break
        elif userInput == "1":
            editScores(selectedGame)
        elif userInput == "2":
            switchGameStatus(selectedGame)

def editScores(gameInQuestion):
    h.titleMe("Edit Scores", False)
    for p in gameInQuestion['Players']:
        print(f'Player: {p["Name"]:<20} | Score: {p["Score"]}')
    while True:
        playerSelect = input("\nPlease enter the name of the player (blank to return):   ").capitalize()
        if playerSelect == "":
            return gameInQuestion
        elif playerSelect not in gameInQuestion['Players']:
            print("That player does not exist!")
        else:
            try:
                while True:
                    scoreInput = int(input("Please enter the new score for the player:   "))
                    if scoreInput < 0:
                        print("You cannot have a score less than zero!")
                    else:
                        gameInQuestion['Players'][playerSelect] = scoreInput
                        
            except ValueError:
                print("That was not a valid input! Please try again!")




def archiveOrActivate(status):
    if status == "Active":
        return "Archive"
    elif status == "Archived":
        return "Re-activate"

def defaultGameListing():
    gameListing = {
        "DateTimeGenerated":[],
        "Players":{},
        "GameType":"10-Pin",
        "ArchivedAt":None
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
        nameInput = input(f"Please enter the name of player #{i+1}: ").capitalize()
        newListing["Players"][nameInput] = 0
    
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