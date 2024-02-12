# Spaceship program - Pierre Kostantine

import time
captain="Cookie Monster"
location="Earth"
shipName="USS Enterprise"
password="ElmoBestFriend"
numAttempts=1
energyLevel=10
shipLimit=4
closeADoors=True

nAttempt=input("What is your name? ")

while nAttempt != captain and numAttempts != 3:
    print("Incorrect")
    nAttempt = input("What is your name? ")
    numAttempts = numAttempts + 1

if nAttempt != captain:
    print("You are not the captain!\nGoodbye!")
else:
    pAttempt = input("Enter the Password: ")

    while pAttempt != password and numAttempts != 3:
        print("Password incorrect")
        pAttempt = input("Enter the password: ")
        numAttempts = numAttempts + 1

    if pAttempt != password:
        print("You are not the captain!\nGoodbye!")
    else:
        print("Password correct. Welcome to the " + shipName)
        numCrew=input("Captain "+captain+", how many crew passengers are with you today? ")
        numCrew=int(numCrew)
        shipLimit=int(shipLimit)
        if numCrew>=shipLimit:
            numCrewOver=numCrew-shipLimit
            print("Sorry Captain "+captain+", you have ", numCrewOver," crew passengers over the limit.")
        else:

            print("")
            print("The spaceship " + shipName + " is currently visiting " + location + ".")

            choice = ""
            while choice != "/exit":
                print("What would you like to do, " + captain + "?")
                print("Dilithium Crystals at: ", energyLevel, "\b%")
                print("")
                print("a. Travel to another planet")
                print("b. Fire canons")
                print("c. Open the airlock")
                print("d. Send Distress Signal")
                print("e. Return to nearest Starbase")
                print("s. Self-destruct")
                print("/exit to exit")
                print("")
                choice = input("Enter your choice: ")
                if choice == "a":
                    if closeADoors==False:
                        print("Sorry Captain "+captain+", the airlock doors are still open, you cannot travel at this time.")
                        time.sleep(1)
                    else:
                        if energyLevel - 10 < 0:
                            print("You do not have enough energy to travel to " + location)
                        else:
                            destination = input("Where would you like to go? ")
                            print("Leaving "+location)
                            print("Travelling to "+destination)
                            time.sleep(5)
                            print("Arrived at "+destination)
                            location = destination
                            energyLevel = energyLevel - 10
                elif choice == "b":
                    if energyLevel - 5 < 0:
                        print("You do not have enough energy to perform that action. ")
                    else:
                        energyLevel = energyLevel - 5 
                        print("Firing canons")
                        time.sleep(1)
                        print("\a\a"*3)
                        print("BANG!")
                        time.sleep(1)
                elif choice == "c":
                    print("Opening airlock")
                    time.sleep(3)
                    print("Airlock open. Transfering Cookies.")
                    time.sleep(1)
                    print("Cookie transfer complete.")
                    closeADoors=input("Would you like to close the air lock doors? (y/n) ")
                    if closeADoors=="y":
                        time.sleep(3)
                        print("Airlock Closed")
                        closeADoors=True
                    else:
                        closeADoors=False
                elif choice == "d":
                    print("Sending Distress Signal")
                    time.sleep(2)
                    print("Captain "+captain+", the USS Excelsior has answered our distress signal.")
                    time.sleep(8)
                    print("Captain "+captain+", the USS Excelsior has arrived and is transfering energy.")
                    time.sleep(4)
                    print("Captain "+captain+", the energy transfer is complete")
                    energyLevel = 15
                elif choice == "e":
                    print("Attempting to travel to nearest Starbase.")

                    if energyLevel - 10<0:
                        print("You do not have enough energy to return to Starbase. ")
                    else:
                        destination = "Closest Starbase"
                        print ("Leaving "+location)
                        print("Travelling to "+destination)
                        time.sleep(5)
                        print("Arrived at "+destination)
                        location=destination
                        print("Dylithium crystals replaced with new ones.")
                        energyLevel=100
                elif choice=="s":
                    confirm=input("Are you sure you want the ship to self-destruct? (y/n)")
                    if confirm=="y" or confirm=="yes":
                        print("Ship will self-destruct in")
                        print("3")
                        time.sleep(1)
                        print("2")
                        time.sleep(1)
                        print("1")
                        time.sleep(1)
                        print("Goodbye")
                        print("BOOM!")
                        choice="/exit"
                elif choice=="/exit":
                    print("Goodbye")
                else:
                    print("Invalid input. Please select a, b, c, d, e, or s. /exit to exit")