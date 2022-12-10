# Title     :   gamaManager
# Purpose   :   Assists with keeping track of games for BowlingManager2022
#
# Programmer:   Danny, Minto, Athul, and Amal
# Date      :   December 7, 2022
# Reference :   Make arguments optional (https://fedingo.com/how-to-create-python-function-with-optional-arguments)

import dannyHelper as h
import uuid 

PROGRAM_NAME = "Bowling Manager 2022"

bowlingGames = None
bmSettings = None

def gamesMenu(bowlingGames, bmSettings):

    bowlingGames = bowlingGames
    bmSettings = bmSettings

    while True:
        h.titleMe("Games Menu", False)
        print("Please make a selection from the options below:")
        print("1) View current active games")
        print("2) Add new game")
        print("3) Archive all current games")
        print("4) View archived games")
        print("5) Save games to file")
        print("6) Load from file")
        print("E) Return to main menu")

        choice = input("Select an option: ").lower()
        
        if choice == "1":
            printGameList(bowlingGames, bmSettings, "Active")
        elif choice == "2":
            newGame = addGame(bmSettings["TimeOffset"])
            newUUID = str(uuid.uuid4())
            bowlingGames["Active"][newUUID] = newGame
        elif choice == "3":
            switchGameStatus(bowlingGames, bmSettings, True)
        elif choice == "4":
            printGameList(bowlingGames, bmSettings, "Archived")
        elif choice == "5":
            saveGameList(bowlingGames, bmSettings)
        elif choice == "6":
            bowlingGames = loadGames(bowlingGames)
        elif choice == "e":
            return bowlingGames    
        else:
            print("That was not a valid option! Please try again.")

def saveGameList(bowlingGames, bmSettings):
    h.titleMe("Save Bowling Games", False)
    while True:
        saveAsTxt = input("Would you like to save a list of bowling games as a .txt? (y/n, blank to exit):   ").lower()
        if saveAsTxt == "":
            break
        elif saveAsTxt == "y":
            fileToWrite = None
            while fileToWrite == None:
                fileToWrite = h.openFile('a', "File")
            if fileToWrite == "exit":
                break
            fileToWrite.write(h.fileTitle(bmSettings["BusinessName"], bmSettings["TimeOffset"])+"\n")
            fileToWrite.write("\n\nActive Games:\n\n")
            for uuid, game in bowlingGames["Active"].items():
                fileToWrite.write(f"Game ID: {uuid}\n")
                fileToWrite.write(f"Generation Time/Date: {game['DateTimeGenerated'][0]} - {game['DateTimeGenerated'][1]}\n")
                fileToWrite.write(f"Game Type: {game['GameType']}\n\n")
                fileToWrite.write("Players:\n\n")
                ticker = 1
                for p , s in game['Players'].items():
                    fileToWrite.write(f"Player {str(ticker)+'.':<5} {p:<15} | Score: {s}\n")
                    ticker += 1
                fileToWrite.write("\n")

            fileToWrite.write("\n\nArchived Games:\n\n")
            for uuid, game in bowlingGames["Archived"].items():
                fileToWrite.write(f"Game ID: {uuid}\n")
                fileToWrite.write(f"Generation Time/Date: {game['DateTimeGenerated'][0]} - {game['DateTimeGenerated'][1]}\n")
                fileToWrite.write(f"Archive Date/Time: {game['ArchivedAt'][0]} - {game['ArchivedAt'][1]}\n")
                fileToWrite.write(f"Game Type: {game['GameType']}\n\n")
                fileToWrite.write("Players:\n\n")
                ticker = 1
                for p , s in game['Players'].items():
                    fileToWrite.write(f"Player {str(ticker)+'.':<5} {p:<15} | Score: {s}\n")
                    ticker += 1
                fileToWrite.write("\n")       

            fileToWrite.write("\n")
            fileToWrite.close()
            print("File saved!")
            input("Press ENTER to return to the main menu...")
            break

        elif saveAsTxt == "n":  # DW - Pickle the inventory for use for loading inventories
            pickleResult = -1
            while pickleResult != 0:
                pickleResult = h.pickleFile(bowlingGames)  # DW - Keep on attempting this command until success
            print("File saved!")
            input("Press ENTER to return to the main menu...")
            break
        else:
            print("Please enter a valid selection!")

def loadGames(ogList):
    h.titleMe("Load Games List", False)
    while True:
        userInput = input("Would you like to load an existing games list from a .dat file? (y/n):   ").lower()
        if userInput == "y":
            loadSuccess = h.openFile('rb', "File", True)
            if loadSuccess == "exit":
                return ogList
            elif loadSuccess == None:
                return ogList
            else:
                if "Active" in loadSuccess and "Archived" in loadSuccess:
                    return loadSuccess
                else:
                    print("This file appears to be incorrect!")
                    return ogList
        elif userInput == "n":
            return ogList

def printGameList(bowlingGames, bmSettings, gameStatus):
    while True:
        h.titleMe(f"{gameStatus} Games List", False)
        gamesList = bowlingGames[gameStatus]
        selectionToUUID = []
        selectedGame = None

        ticker = 0
        for u in gamesList.keys():
            selectionToUUID.append(u)
            print(f"{ticker+1}) {len(gamesList[u]['Players'])}-player, {gamesList[u]['GameType']} game @ {gamesList[u]['DateTimeGenerated'][1]}")
            ticker += 1
        selectedGame = input("\nPlease select a game you wish to view (blank to return to menu):   ")
        if selectedGame == "":
            return bowlingGames
        else:
            try:
                selectedGame = selectionToUUID[int(selectedGame) - 1]
                bowlingGames = viewListing(selectedGame, gameStatus, bowlingGames, bmSettings)
            except ValueError:
                print("That was not a valid input, please try again!")
            except EOFError:
                print("That was not a valid input, please try again!")

def viewListing(gameUUID, gameStatus, bowlingGames, bmSettings):
    while True:
        h.titleMe("View Listing", False)
        selectedGame = bowlingGames[gameStatus][gameUUID]

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
            return bowlingGames
        elif userInput == "1":
            bowlingGames = editScores(bowlingGames, gameUUID, gameStatus)
        elif userInput == "2":
            bowlingGames, gameStatus = switchGameStatus(bowlingGames, bmSettings, False, gameUUID, gameStatus)

def editScores(bowlingGames, gameUUID, gameStatus):
    h.titleMe("Edit Scores", False)
    gameInQuestion = bowlingGames[gameStatus][gameUUID]
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
                        bowlingGames[gameStatus][gameUUID] = gameInQuestion
                        return bowlingGames        
                except ValueError:
                    print("That was not a valid input! Please try again!")

def switchGameStatus(bowlingGames, bmSettings, archiveAll, gameUUID = None, gameStatus = None):
    h.titleMe("Switch Game Status", False)
    while True:
        if archiveAll:
            userInput = input("Archive all active games? (y/n):   ").lower()
            if userInput == "y":
                for key in bowlingGames["Active"].keys():
                    bowlingGames["Archived"][key] = bowlingGames["Active"][key]
                    genTime = h.timeMe(bmSettings["TimeOffset"])
                    bowlingGames["Archived"][key]["ArchivedAt"] = [genTime[0], genTime[1]]
                bowlingGames["Active"] = {}
                input("Active games archived! Press ENTER to continue...")
                return bowlingGames
            elif userInput == "n":
                return bowlingGames
        else:
            userInput = input("Switch this game's status? (y/n):   ").lower()
            if userInput == "y":
                returnStatus = None
                copyMii = bowlingGames[gameStatus][gameUUID]
                if gameStatus == "Active":
                    bowlingGames["Archived"][gameUUID] = copyMii
                    genTime = h.timeMe(bmSettings["TimeOffset"])
                    bowlingGames["Archived"][gameUUID]["ArchivedAt"] = [genTime[0], genTime[1]]
                    returnStatus = "Archived"
                else:
                    bowlingGames["Active"][gameUUID] = copyMii
                    bowlingGames["Active"][gameUUID]["ArchivedAt"] = None
                    returnStatus = "Active"
                bowlingGames[gameStatus].pop(gameUUID)
                input("Game status changed! Press ENTER to continue...")
                return bowlingGames, returnStatus
            elif userInput == "n":
                return bowlingGames, returnStatus

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