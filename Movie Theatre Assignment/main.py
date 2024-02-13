# Movie Theatre - Pierre Kostantine

from ExtensionsToInput import * #Used this to ensure that the user inputs a valid amount of the same item they would like to purchase
import random #Used this for the discount game at the end
import math #Used for checkout
import time #Used this for making the UI cleaner by putting delays in between different menus and reponses
import sys #Used this to end the system when program finished

lgpc="" #Used these to make sure that any items that aren't bought dont crash the checkout and the totalBeforeDiscount variable
mdpc=""
smpc=""
coke=""
sprite=""
nestea=""
hotDog=""
lgpcTotal=0 #Used these to make sure that any items that aren't bought dont crash the checkout and the totalBeforeDiscount variable
mdpcTotal=0
smpcTotal=0
cokeTotal=0
spriteTotal=0
nesteaTotal=0
hotDogTotal=0
movieTotal=0
amountOfTickets=0
movieChoice="" #Used this to make sure that it doesnt crash the first while statement
foodChoice="" #Used this to make sure that it doesnt crash the second while statement


print("Welcome to Filmeplex!")
while movieChoice!="a" or movieChoice!="b" or movieChoice!="c" or movieChoice!="d": #If user inputs a false input it will send them back here
    movieChoice=input("What Movie would you like to watch?\na.\tBlack Panther: Wakanda Forever\nb.\tAfter sun\nc.\tAvatar 2\nd.\tTruman Show\n")
    movieChoice=movieChoice.strip().lower() #allows room for mistakes from the user while entering their answer by removing any spaces and capitals
    clearOrder=""
    if movieChoice=="a" or movieChoice=="b" or movieChoice=="c" or movieChoice=="d":
        amountOfTickets=inputIntLow("How many tickets would you like to purchase? ($15 each)\t",0) #inputIntLow makes it so that the user cannot enter an number with decimals nor a number below 0
        movieTotal=15*amountOfTickets #calculates the total for the movie section for checkout
        while foodChoice!="e": #If user inputs a false input it will send them back here
            print("Here are the different groups of items we have available to search through:\n")
            print("a.\tPopcorn")
            print("b.\tDrinks")
            print("c.\tHot Dogs")
            print("d.\tCheckout.\n")
            foodChoice=input("Which items would you like to search through?\t")
            foodChoice=foodChoice.strip().lower()
            if foodChoice=="a":
                lgpcPrice=9 #the price variables are used to display the prices and calculate the total
                mdpcPrice=8
                smpcPrice=6
                print("1. Large\t$",lgpcPrice)
                print("2. Medium\t$",mdpcPrice)
                print("3. Small\t$",smpcPrice)
                print("4. Go back to the main menu.\n")
                pcChoice=input("Please enter your choice:\t")
                pcChoice=pcChoice.strip().lower()
                if pcChoice=="1":
                    lgpcAmount=inputIntLow("\nHow many would you like to purchase\t",0)
                    lgpc=True #helps the checkout know which items to display
                    lgpcTotal=lgpcAmount*lgpcPrice
                elif pcChoice=="2":
                    mdpcAmount=inputIntLow("\nHow many would you like to purchase\t",0)
                    mdpc=True
                    mdpcTotal=mdpcAmount*mdpcPrice
                elif pcChoice=="3":
                    smpcAmount=inputIntLow("\nHow many would you like to purchase\t",0)
                    smpc=True
                    smpcTotal=smpcAmount*smpcPrice
                elif pcChoice=="4":
                    foodChoice==""
                else:
                    print("\nInvalid input, please try again")
                    time.sleep(1) #makes the code wait 1 second before displaying the menu again
            elif foodChoice=="b":
                cokePrice=3
                spritePrice=2
                nesteaPrice=2.5
                print("1. Coke\t\t$",cokePrice)
                print("2. Sprite\t$",spritePrice)
                print("3. Nestea\t$",nesteaPrice)
                print("4. Go back to the main menu.\n")
                drinkChoice=input("Please enter your choice:\t")
                drinkChoice=drinkChoice.strip().lower()
                if drinkChoice=="1":
                    cokeAmount=inputIntLow("\nHow many would you like to purchase\t",0)
                    coke=True 
                    cokeTotal=cokeAmount*cokePrice
                elif drinkChoice=="2":
                    spriteAmount=inputIntLow("\nHow many would you like to purchase\t",0)
                    sprite=True
                    spriteTotal=spriteAmount*spritePrice
                elif drinkChoice=="3":
                    nesteaAmount=inputIntLow("\nHow many would you like to purchase\t",0)
                    nestea=True
                    nesteaTotal=nesteaAmount*nesteaPrice
                elif drinkChoice=="4":
                    foodChoice==""
                else:
                    print("\nInvalid input, please try again")
                    time.sleep(1)
            elif foodChoice=="c":
                hotDogPrice=4 #the price variables are used to display the prices and calculate the total
                print("1. Hot Dog\t$",hotDogPrice)
                print("2. Go back to the main menu.\n")
                hotDogChoice=input("Please enter your choice:\t")
                hotDogChoice=hotDogChoice.strip().lower()
                if hotDogChoice=="1":
                    hotDogAmount=inputIntLow("\nHow many would you like to purchase\t",0)
                    hotDog=True
                    hotDogTotal=hotDogAmount*hotDogPrice
                elif hotDogChoice=="4":
                    foodChoice==""
                else:
                    print("\nInvalid input, please try again")
                    time.sleep(1)
            elif foodChoice=="d":
                clearOrder=input("Would you like to clear your order? (y/n)\t")
                if clearOrder=="y":
                    clearOrder=input("Are you sure you want to clear your order and restart? (y/n)\t")
                    if clearOrder=="y": #Used to reset all the checkout values in order to clear the cart
                        lgpc=""
                        mdpc=""
                        smpc=""
                        coke=""
                        nestea=""
                        sprite=""
                        hotDog=""
                        lgpcTotal=0
                        mdpcTotal=0
                        smpcTotal=0
                        cokeTotal=0
                        spriteTotal=0
                        nesteaTotal=0
                        hotDogTotal=0
                        discount=False
                if clearOrder!="y":
                    discountGame=input("Before you checkout, would you like to answer a random multiplication question for a chance at a 5 percent discount? (y/n) ")
                    if discountGame=="y" or discountGame=="yes":
                        x=random.randint(2,12)
                        y=random.randint(2,12)
                        print("What is",x,"*",y,"?")
                        multiplicationInput = float(input("Your Guess: "))
                        if multiplicationInput == x*y:
                            print("Correct!")
                            time.sleep(1)
                            discount=True
                        else:
                            print("Sorry, the answer you entered is incorrect.")
                            time.sleep(2)
                            discount=False
                    elif discountGame=="n":
                        print("aww :(")
                        time.sleep(1)
                        discount=False
                    else:
                        print("Invalid input, please try again.")
                        choice="/checkout"
                        discount=False
                    print("These are the items in your cart\n")
                    print(amountOfTickets,"x\tMovie Tickets \t$ 15")
                    if lgpc==True: #these if statements make sure that only the items that are bought are displayed
                        print(lgpcAmount,"x\tLarge Popcorn \t$",lgpcPrice) #these lines print the amount of the same item and its individual price
                    if smpc==True:
                        print(smpcAmount,"x\tMedium Popcorn \t$",smpcPrice)
                    if mdpc==True:
                        print(mdpcAmount,"x\tSmall Popcorn \t$",mdpcPrice)
                    if coke==True:
                        print(cokeAmount,"x\tCoke \t$",cokePrice)
                    if sprite==True:
                        print(spriteAmount,"x\tSprite \t$",spritePrice)
                    if nestea==True:
                        print(nesteaAmount,"x\tNestea \t$",nesteaPrice)
                    if hotDog==True:
                        print(hotDogAmount,"x\tHot Dog \t$",hotDogPrice)
                    priceBeforeDiscount=movieTotal+lgpcTotal+mdpcTotal+smpcTotal+cokeTotal+spriteTotal+nesteaTotal+hotDogTotal
                    priceAfterDiscount=priceBeforeDiscount*0.95
                    if discount==True:
                        print("Your total without the discount is $",priceBeforeDiscount)
                        print("Discount = -5%")
                        print("\nYour subtotal is $",priceAfterDiscount)
                        total=priceAfterDiscount*1.13
                        print("\nYour total is $",total)
                    else:
                        print("\nYour subtotal is $",priceBeforeDiscount)
                        total=priceBeforeDiscount*1.13
                        print("\nYour total is $",total)
                    paymentComplete=False
                    while paymentComplete==False: #redisplays payment options if user enters invalid input
                        time.sleep(2)
                        print("How would you like to pay?")
                        print("a. Paypal")
                        print("b. Credit Card")
                        paychoice=input("Your choice:\t")
                        if paychoice=="a":
                            paypalEmail=input("Email: ")
                            paypalPassword=input("Password: ")
                            print("Payment Successful!\nEnjoy your movie!")
                            paymentComplete=True
                            sys.exit()
                        elif paychoice=="b":
                            ccNumber=input("Credit Card Number: (i hope i dont have to say this but PLEASE DONT actually enter it)")
                            ccExpiryDate=input("Expiry Date: ")
                            ccCVV=input("CVV (on the back of the card): ")
                            print("Payment Successful!\nEnjoy your movie!")
                            paymentComplete=True
                            sys.exit()
                        else:
                            print("Invalid input, please select a proper payment method")
            else:
                print("Invalid input, please try again.")
                time.sleep(1)
        else:
            print("Invalid input, please try again.")
            time.sleep(1)
    else:
        print("Invalid input, please try again.")
        time.sleep(1)