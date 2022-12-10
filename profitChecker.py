# Title     :   profitChecker
# Purpose   :   Helper module for my programs to streamline development
#
# Programmer:   Danny, Athul, Amal, and Minto
# Date      :   December 10, 2022
# Reference :

import dannyHelper as h

def checkProfits(bowlingGames, currentConfig):
    h.titleMe("Check Today's Profits", False)

    totalProfits = [0, 0]   # DW - List with two indexes (first is active, second is archived)
    print("Calculating...")
    # DW - Calculate total cash made from currently active and archived games
    for info in bowlingGames["Active"].values():
        totalProfits[0] += currentConfig["BaseGamePrice"] + (len(info["Players"]) *  currentConfig["PricePerPlayer"])
    for info in bowlingGames["Archived"].values():
        totalProfits[1] += currentConfig["BaseGamePrice"] + (len(info["Players"]) *  currentConfig["PricePerPlayer"])
    
    print(f"Total Active Games Profit:   $ {totalProfits[0]:,.2f}")
    print(f"Total Archived Games Profit: $ {totalProfits[1]:,.2f}")
    print(f"\nTotal Profits Today:         $ {totalProfits[0]+totalProfits[1]:,.2f}")

    input("Press ENTER to return to the main menu...")