# Title     :   dannyHelper
# Purpose   :   Helper module for my programs to streamline development
#
# Programmer:   Danny Wakeling
# Date      :   November 21, 2022
# Reference :

import datetime
import pickle
from time import sleep

def additionalSigns(inputString, isEqualSign):
    returnString = "" # Make a blank string
    if isEqualSign:
        for i in range(0, len(inputString)):
            returnString += "=" # Add a sign for each individual character in the input string
    else:
        for i in range(0, len(inputString)):
            returnString += "-"
    return returnString

def isPlural(inputNumber):
    if inputNumber != 1: # Is it not 1?
        return "s"
    else: # It is 1!
        return ""

def titleMe(PROGRAM_NAME, isMainTitle):
    PROGRAMMER = "Danny, Minto, Athul, and Amal"
    if isMainTitle:
        print(f"\n\tWelcome to {PROGRAM_NAME}! | Programmed by {PROGRAMMER}\n\t{additionalSigns(f'Welcome To {PROGRAM_NAME}! | Programmed by {PROGRAMMER}', True)}\n")
    else:
        print(f"\n{PROGRAM_NAME}\n{additionalSigns(f'{PROGRAM_NAME}', False)}\n")

def timeMe(tzOffset):
    tzinfo = datetime.timezone(datetime.timedelta(hours=tzOffset))
    dateTimeNow = datetime.datetime.now(tzinfo).strftime("%B %d, %Y - %I:%M:%S %p").split(" - ")
    return dateTimeNow

def fileTitle(inputText):
    dateTimeNow = timeMe()
    return f"\t{inputText}   |   Recorded {dateTimeNow}\n\t{additionalSigns(f'{inputText}   |   Recorded {dateTimeNow}', False)}\n"

def isExitFromNone(exitIfNone):
    if exitIfNone:
        return " (leave blank to load default config)"

def openFile(writeMode, exitIfNone):
    tempName = input(f"Please enter a file name to read from{isExitFromNone(exitIfNone)}:   ")
    try:
        if tempName == "":
            if exitIfNone:
                print("Goodbye!")
                return "exit"
            else:
                print("Please enter a file name!")
                return None
        FILE_NAME = (tempName.split(".txt"))[0]+".txt"
        print(f"Now reading from {FILE_NAME}...\n")
        returnFile = open(FILE_NAME, writeMode)
        sleep(0.25)
        return returnFile
    except FileNotFoundError as e:    #   File could not be opened
        print(e)
        sleep(0.5)
        print("\nSorry, we couldn't open your file! Please try again...")
        sleep(0.5)
        return None
            
def pickleFile(inputFile):
    tempName = input("Please enter the name you would like to save the file as:   ")
    if tempName == "":
        print("Please enter a file name!")
        return 1
    else:
        tempName = tempName.split(".dat")[0]+".dat"
    try:
        fileToOutput = open(tempName, "wb")
        pickle.dump(inputFile, fileToOutput)
        print("Finished!")
        fileToOutput.close()
        return 0
    except IOError as e:
        print(e)
        sleep(0.5)
        print("\nSorry, we couldn't save your file! Please try again...")
        sleep(0.5)
        return 1