#This program will let the user enter the names for 12 players of a football team.
#It will then prompt the user to enter stats about At bats and Hits.
#The final output will be a table with name, at bats, hits and average.
#
#Nico Busatto 04/15/2019

import os
import time
import math

counter = 0

def main():
    
    option = 5
    Good = True   # Main() loop control
   
    while option > 4 or not Good:

        global counter
        
        try:
            
            if counter == 0:
                counter += 1
                print(" ____  __      __   _  _  ____    __    __    __   /\/\ ")
                print("(  _ \(  )    /__\ ( \/ )(  _ \  /__\  (  )  (  )  )()(")
                print(" )___/ )(__  /(__)\ \  /  ) _ < /(__)\  )(__  )(__ \/\/")
                print("(__)  (____)(__)(__)(__) (____/(__)(__)(____)(____)()()")
                print("By Nico Busatto")
                print("")
                playerN = playerNames()
            print("1 - Enter players name")
            print("2 - Enter player statistics")
            print("3 - Summary Display")
            print("4 - Exit")
            print("")
            option = int(input("Enter option: (1, 2, 3, 4): ")) #menu option input
            if (option > 4):
                print("")
                print("Wrong entry, please enter a number from 1 to 4")
                Good = False
            if option == 1:
                playerN = playerNames()
                option = 5
                Good = True
            elif option == 2:
                counter += 1
                playerBats, playerHits = playerStats(playerN)
                option = 5
                Good = True
            elif option == 3 and counter < 2:
                print("")
                print("Insert some stats first.")
                print("")
                Good = False
            elif option == 3 and counter >= 2:
                playerAvg = calcs(playerBats, playerHits)
                displaySum(playerN, playerBats, playerHits, playerAvg)
                option = 5
                Good = True
            else:
                exit()
        except ValueError:                  #Catch value exception
            print("")
            print("Wrong entry, please enter a number from 1 to 4")
            Good = False

def playerNames():
    
    playerN = []                            #Create list for names

    for y in range(12):
        try:
            playerN.append(input("Enter name for player Number " + str(y + 1) + ": "))
        except ValueError:
            print("Please enter a name")

    print("")
    print("The name inserted are: ")
    print(playerN)
    print("")

    return playerN
    
def playerStats(playerN):
    
    playerBats = [0 for x in range(12)]    #Initialize lists for At bats and Hits values
    playerHits = [0 for x in range(12)]
    keepGoing = 'y'                         #playerStats() loop control
    Good = True                             #At bats and Hits validation loop control
    Good2 = True                            #Next entry loop control 
    hitsBatsOk = True                       #Validation for hits lower than at bats

    while keepGoing == 'y':
        try:
            playerNumOk = True              #Player number validation loop control
            player = int(input("Select player number (1 - 12): "))
            while playerNumOk:
                if player > 12:
                    print("Player number must be between 1 - 12, please re-enter.")
                    player = int(input("Select player number (1 - 12): "))
                else:
                    playerNumOk = False
                    Good = True
                    Good2 = True
                    hitsBatsOk = True
            while Good:
                    playerBats[player - 1] += int(input("Enter number of times At Bats: "))
                    playerHits[player - 1] += int(input("Enter number of Hits: "))
                    while hitsBatsOk:
                        #if playerHits[player] > playerBats[player]:
                            #print("Hits can't be greater than At bats, please re-enter dear.")
                            #playerBats[player - 1] += int(input("Enter number of times At Bats: "))
                            #playerHits[player - 1] += int(input("Enter number of Hits: "))
                            #print("")
                        print("")
                        keepGoing = input("Do you want to enter another stat?: ")
                        while Good2:
                            if keepGoing != 'y' and keepGoing != 'n':
                                    keepGoing = input("Yes(y) or No(n)?")
                            if keepGoing == 'y':
                                Good = False
                                Good2 = False
                                hitsBatsOk = False
                                PlayerNumOk = False
                            elif keepGoing == 'n':
                                Good = False
                                Good2 = False
                                PlayerNumOk = False
                                hitsBatsOk = False
        except ValueError:
                    print("")
                    print("Only numbers allowed.")
                    Good = False

    return playerBats, playerHits

def calcs(bats, hits):

    Good = True
    playerAvg = [0 for x in range(12)]                           #Initialize player average list

    while Good:
        for y in range(12):
                try:
                    playerAvg[y] = round((hits[y] / bats[y]),3)      #Calc player average
                except ZeroDivisionError:                           #Catch divisions by 0
                    playerAvg[y] = 0
                    Good = False

    return playerAvg

def displaySum(name = [], bats = [], hits = [], avg = []):

    y = 0

    print("")
    print("Player Name\t\t\tAt Bats\t\t\t\tHits\t\t\t\tAverage")
    print("----------------------------------------------------------------------------------------------------------")

    for y in range(12):                                 #Format and print final table with a for loop
        print(str('{:<20}'.format(name[y])), str('{:^30}'.format(bats[y]).strip('[]')), str('{:^30}'.format(hits[y]).strip('[]')), str("{:^30}".format(avg[y]).strip('[]')))
    print("")

def exit():

    print("Program ending, have a good one!")
    time.sleep(4)
    os._exit(1)

main()