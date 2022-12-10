# Title     :   gamaManager
# Purpose   :   Assists with keeping track of games for BowlingManager2022
#
# Programmer:   Danny, Minto, Athul, and Amal
# Date      :   December 7, 2022
# Reference :   Make arguments optional (https://fedingo.com/how-to-create-python-function-with-optional-arguments)

import dannyHelper as h
import uuid 

PROGRAM_NAME = "Bowling Manager 2022"

bowlingList = None
activeSettings = None

def gamesMenu(bowlingGames, bmSettings):
    global bowlingList
    global activeSettings

    bowlingList = bowlingGames
    activeSettings = bmSettings

    while True:
        h.titleMe("Games Menu", False)
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
            newUUID = uuid.uuid4()
            bowlingGames["Active"][newUUID] = newGame
        elif choice == "3":
            switchGameStatus(True)
        elif choice == "4":
            printGameList("Archived")
        elif choice == "e":
            break    
        else:
            print("That was not a valid option! Please try again.")

def printGameList(gameStatus):
    while True:
        h.titleMe(f"{gameStatus} Games List", False)
        gamesList = bowlingList[gameStatus]
        selectionToUUID = []
        selectedGame = None

        ticker = 0
        for u in gamesList.keys():
            selectionToUUID.append(u)
            print(f"{ticker+1}) {len(gamesList[u]['Players'])}-player, {gamesList[u]['GameType']} game @ {gamesList[u]['DateTimeGenerated'][1]}")
            ticker += 1
        selectedGame = input("\nPlease select a game you wish to view (blank to return to menu):   ")
        if selectedGame == "":
            break
        else:
            try:
                selectedGame = selectionToUUID[int(selectedGame) - 1]
                viewListing(selectedGame, gameStatus)
            except ValueError:
                print("That was not a valid input, please try again!")
            except EOFError:
                print("That was not a valid input, please try again!")

def viewListing(gameUUID, gameStatus):
    while True:
        h.titleMe("View Listing", False)
        selectedGame = bowlingList[gameStatus][gameUUID]

        print(f"Generation Time/Date: {selectedGame['DateTimeGenerated'][0]} - {selectedGame['DateTimeGenerated'][1]}")
        print(f"Game status: {gameStatus}")

        if gameStatus == "Archived":
            print(f"Archive time: {selectedGame['ArchivedAt'][0]} - {selectedGame['ArchivedAt'][1]}")
        
        print(f"\nGame Type: {selectedGame['GameType']}")

        print(f"Players:\n")
        ticker = 1
        for p , s in selectedGame['Players'].items():
            print(f"Player {str(ticker)+'.':<5} {p:<15} | Score: {s}")
            ticker += 1

        print("\nYou can make the following options"+
        f"\n1) Edit the score of a player\n2) {archiveOrActivate(gameStatus)} this game\nR) Return to the game list")

        userInput = input("\nPlease make a selection:   ").lower()
        if userInput == "r":
            break
        elif userInput == "1":
            editScores(gameUUID, gameStatus)
        elif userInput == "2":
            gameStatus = switchGameStatus(False, gameUUID, gameStatus)

def editScores(gameUUID, gameStatus):
    global bowlingList
    h.titleMe("Edit Scores", False)
    gameInQuestion = bowlingList[gameStatus][gameUUID]
    for p, s in gameInQuestion['Players'].items():
        print(f'Player: {p:<20} | Score: {s}')
    while True:
        playerSelect = input("\nPlease enter the name of the player (blank to return):   ").capitalize()
        if playerSelect == "":
            return gameInQuestion
        elif playerSelect not in gameInQuestion['Players']:
            print("That player does not exist!")
        else:
            while True:
                try:
                    scoreInput = int(input("Please enter the new score for the player:   "))
                    if scoreInput < 0:
                        print("You cannot have a score less than zero!")
                    else:
                        gameInQuestion['Players'][playerSelect] = scoreInput
                        bowlingList[gameStatus][gameUUID] = gameInQuestion
                        break        
                except ValueError:
                    print("That was not a valid input! Please try again!")

def switchGameStatus(archiveAll, gameUUID = None, gameStatus = None):
    global bowlingList
    h.titleMe("Switch Game Status", False)
    while True:
        if archiveAll:
            userInput = input("Archive all active games? (y/n):   ").lower()
            if userInput == "y":
                for key in bowlingList["Active"].keys():
                    bowlingList["Archived"][key] = bowlingList["Active"][key]
                    genTime = h.timeMe(activeSettings["TimeOffset"])
                    bowlingList["Archived"][key]["ArchivedAt"] = [genTime[0], genTime[1]]
                bowlingList["Active"] = {}
                input("Active games archived! Press ENTER to continue...")
                break
            elif userInput == "n":
                break
        else:
            userInput = input("Switch this game's status? (y/n):   ").lower()
            if userInput == "y":
                returnStatus = None
                copyMii = bowlingList[gameStatus][gameUUID]
                if gameStatus == "Active":
                    bowlingList["Archived"][gameUUID] = copyMii
                    genTime = h.timeMe(activeSettings["TimeOffset"])
                    bowlingList["Archived"][gameUUID]["ArchivedAt"] = [genTime[0], genTime[1]]
                    returnStatus = "Archived"
                else:
                    bowlingList["Active"][gameUUID] = copyMii
                    bowlingList["Active"][gameUUID]["ArchivedAt"] = None
                    returnStatus = "Active"
                bowlingList[gameStatus].pop(gameUUID)
                input("Game status changed! Press ENTER to continue...")
                return returnStatus
            elif userInput == "n":
                break

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
            if amountOfPlayers < 1:
                print("You can't have less than one player!")
                continue
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