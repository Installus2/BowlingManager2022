# Title     :casestudy 
# Purpose   : bowling manager 
#
# Programmer: Amal,Athul,Danny,Minto 
# Date      :3 DEC 2022
# Reference :

#different options for selecting users need.
#Bowling score calculaor
#scores write in a file

import csv


def main():
   
    while True:
         #create menu options
        print("--------Main Menu--------")       
        print("Welcome to the bowling alley! What would you like to do?")
        print("1. Active bowling games")
        print("2. Archived bowling games")
        print("3. Inventory")
        print("4. Today's Profits")
        print("5.Price & Options")
        print("6.Exit")
        
        option = input("Select an option: ")
       
        if option == "1":
            viewGames()
       
        elif option == "2":
            addGame()
       
        elif option == "3":
            archiveGames()
        
        elif option == "4":
            profit()
        elif option == "5":
            price()
        elif option == "6":
            print("Exiting program.....")
            break
       
        else:
            print("Please select a valid option")

#menu options inside viewgames.
def viewGames():
   
   print("a)View current active games")
   print("b)Add new active game")
   print("c)Archive all current games")
   print("d)score calculator")
   print("e)Return to main menu")

   choice = input("Select an choice: ")
   
   if choice == "a":
        viewOpenGames()
       
   elif choice == "b":
       
        addGame()
       
   elif choice == "c":
        archiveGames()
        
   elif choice == "d":
       scorecalculator()
       
   elif choice == "e":
       
        main()
       
   else:
       print("please enter correct option")

def viewOpenGames():
    #To open a old game.
    username = input("Please enter username")
    filename = open(username, "r")
    print()
    #To print without bracket & comma   
    separator=""
    print(separator.join(filename))
      
#for starting a new bowling game        
def addGame():
    print("Add a new game")

#bowling histories
def archiveGames():
    print("Archive all current games")
      
#bowling score calculator       
def scorecalculator():
   #its better to ask username for everytime so, later  user information can be pulled easily.
    username = input('please enter a username ')
    totalscore = open(username,'w')
    print("The total number of rounds are 9")
                     
    score = 0
    c = 0 

    def print_score(frame,score):
        print("\n Score after {0} frame is {1}".format(frame+1,score))

    for frame in range(10):
        roll_1 = 0
        roll_2 = 0
        roll_1 = int(input('\n Pin dropped in first roll: '))
        if roll_1 == 10:
            score += 10
            print_score(frame,score)
            if c == 1 or c == 2:
                score += 10
            c = 1
        else:
            roll_2 = int(input('\n Pin dropped in second roll: '))
            if c == 1:
                score += roll_1 + roll_2
            if c == 2:
                score += roll_1
            if (roll_1 + roll_2) == 10 :
                score += 10
                c = 2
                print_score(frame,score)
            else:
                score += roll_1 + roll_2
                c = 0
                print_score(frame,score)
        if frame == 9:
            if c == 1:
                r1 = int(input('\n Pin dropped in bonus first roll: '))
                if r1 == 10:
                    score += 10
                    print("Total score {}".format(score))
                else:
                    r2 = int(input('\nPin dropped in bonus second roll: '))
                    score += r1 + r2 
                    print("Total score {}".format(score))
            elif c == 2:
                r1 = int(input('\n Pin dropped in bonus first roll: '))
                score += r1
                print("Total score {}".format(score))
            else:
                print("Total score {}".format(score))

        totalscore.write(str(roll_1))
        totalscore.write("\t")
        totalscore.write(str(roll_2))
        totalscore.write("\n")
    totalscore.close()
        



main()
