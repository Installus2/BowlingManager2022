# Title     :   gamaManager
# Purpose   :   Assists with keeping track of games for BowlingManager2022
#
# Programmer:   Danny, Minto, Athul, and Amal
# Date      :   December 7, 2022
# Reference :   

import dannyHelper as h

def gamesMenu():
   while True:
    print(f"\n{h.titleMe('Games Menu', False)}")
    print("Please make a selection from the options below:")
    print("1) View current active games")
    print("2) Add new game")
    print("3) Archive all current games")
    print("4) score calculator")
    print("E) Return to main menu")

    choice = input("Select an option: ").lower()
    
    if choice == "a":
            viewActiveGames()
        
    elif choice == "b":
        
            addGame()
        
    elif choice == "c":
            archiveGames()
            
    elif choice == "d":
        scorecalculator()
        
    elif choice == "e":
            break
        
    else:
        print("please enter correct option")

def viewActiveGames():
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