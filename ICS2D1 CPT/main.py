# DJ Store - Pierre Kostantine

from ExtensionsToInput import * #Used this to ensure that the user inputs a valid amount of the same item they would like to purchase
import random #Used this for the discount game at the end
import math #Used for checkout
import time #Used this for making the UI cleaner by putting delays in between different menus and reponses

sDMic="" #Used these to make sure that any items that aren't bought dont crash the checkout and the totalBeforeDiscount variable
sCMic=""
nBMic=""
sisMKb=""
mdmMKb=""
sisMixer=""
reg1Mixer=""
reg2Mixer=""
cRInterface=""
nBTriStand=""
samTriStand=""
nBDeskStand=""
sDMicTotal=0 #Used these to make sure that any items that aren't bought dont crash the checkout and the totalBeforeDiscount variable
sCMicTotal=0
nBMicTotal=0
sisMKbTotal=0
mdmMKbTotal=0
sisMixerTotal=0
reg1MixerTotal=0
reg2MixerTotal=0
cRInterfaceTotal=0
nBTriStandTotal=0
samTriStandTotal=0
nBDeskStandTotal=0
choice="" #Used this to make sure that it doesnt crash the "while choice!="/checkout":" line
print("Welcome to Canada's DJs Online Store!")
while choice!="/checkout":
    print("Here are the different groups of items we have available to search through:\n")
    print("a. Microphones")
    print("b. MIDI Keyboards")
    print("c. Audio Mixers and Interfaces")
    print("d. Microphone Stands")
    print("/checkout to checkout.\n")
    choice=input("Which items would you like to search through?\t")
    choice=choice.strip().lower()
    if choice=="a":
        sDMicPrice=100 #the price variables are used to display the prices and calculate the total
        sCMicPrice=70
        nBMicPrice=40
        print("Here is our list of microphones available to purchase:\n")
        print("1. Sure Dynamic Microphone\t$",sDMicPrice)
        print("2. Sure Condenser Microphone\tON SALE! $",sCMicPrice,"(was $100)")
        print("3. NozamaBasics Microphone\t$",nBMicPrice)
        print("/return to go back to the main menu.\n")
        micChoice=input("Please enter your choice:\t")
        micChoice=micChoice.strip().lower()
        if micChoice=="1":
            sDMicAmount=inputFloatLow("\nHow many would you like to purchase\t",0) #this common line and the 7 below it are used to make sure that the user inputs a valid number
            if sDMicAmount!=int(sDMicAmount):
                print("Please enter a valid float integer value")
                sDMicAmount=0
                time.sleep(1)
            else:
                sDMic=True #helps the /checkout know which items to display
                sDMicTotal=sDMicAmount*sDMicPrice
        elif micChoice=="2":
            sCMicAmount=inputFloatLow("\nHow many would you like to purchase\t",0)
            if sCMicAmount!=int(sCMicAmount):
                print("Please enter a valid float integer value")
                sCMicAmount=0
                time.sleep(1)
            else:
                sCMic=True
                sCMicTotal=sCMicAmount*sCMicPrice
        elif micChoice=="3":
            nBMicAmount=inputFloatLow("\nHow many would you like to purchase\t",0)
            if nBMicAmount!=int(nBMicAmount):
                print("Please enter a valid float integer value")
                nBMicAmount=0
                time.sleep(1)
            else:
                nBMic=True
                nBMicTotal=nBMicAmount*nBMicPrice
        elif micChoice=="/return":
            choice==""
        else:
            print("\nInvalid input, please try again")
            time.sleep(1)
    elif choice=="b":
        sisMKbPrice=120
        mdmMKbPrice=60
        print("Here is our list of MIDI Keyboards available to purchase:\n")
        print("1. Sisela MIDI Keyboard \t$",sisMKbPrice)
        print("2. midiminus MIDI Keyboard\t$",mdmMKbPrice)
        print("/return to go back to the main menu.\n")
        mKbChoice=input("Please enter your choice:\t")
        mKbChoice=mKbChoice.strip().lower()
        if mKbChoice=="1":
            sisMKbAmount=inputFloatLow("\nHow many would you like to purchase\t",0)
            if sisMKbAmount!=int(sisMKbAmount):
                print("Please enter a valid float integer value")
                sisMKbAmount=0
                time.sleep(1)
            else:
                sisMKb=True
                sisMKbTotal=sisMKbAmount*sisMKbPrice
        elif mKbChoice=="2":
            mdmMKbAmount=inputFloatLow("\nHow many would you like to purchase\t",0)
            if mdmMKbAmount!=int(mdmMKbAmount):
                print("Please enter a valid float integer value")
                mdmMKbAmount=0
                time.sleep(1)
            else:
                mdmMKb=True
                mdmMKbTotal=mdmMKbAmount*mdmMKbPrice
        elif mKbChoice=="/return":
            choice==""
        else:
            print("\nInvalid input, please try again")
            time.sleep(1)
    elif choice=="c":
        sisMixerPrice=130
        reg1MixerPrice=160
        reg2MixerPrice=75
        cRInterfacePrice=100
        print("Here is our list of audio mixers and interfaces available to purchase:\n")
        print("1. Sisela Audio Mixer (4-Channel 2-Bus) \t$",sisMixerPrice)
        print("2. Regnirheb Audio Mixer (10-Channel 2-Bus)\t$",reg1MixerPrice)
        print("3. Regnirheb Audio Mixer (5-Channel 1-Bus)\t$",reg2MixerPrice)
        print("4. ConcentrateRight Audio Interface (1-Bus)\t$",cRInterfacePrice)
        print("/return to go back to the main menu.\n")
        mixerChoice=input("Please enter your choice:\t")
        mixerChoice=mixerChoice.strip().lower()
        if mixerChoice=="1":
            sisMixerAmount=inputFloatLow("\nHow many would you like to purchase\t",0)
            if sisMixerAmount!=int(sisMixerAmount):
                print("Please enter a valid float integer value")
                sisMixerAmount=0
                time.sleep(1)
            else:
                sisMixer=True
                sisMixerTotal=sisMixerAmount*sisMixerPrice
        elif mixerChoice=="2":
            reg1MixerAmount=inputFloatLow("\nHow many would you like to purchase\t",0)
            if reg1MixerAmount!=int(reg1MixerAmount):
                print("Please enter a valid float integer value")
                reg1MixerAmount=0
                time.sleep(1)
            else:
                reg1Mixer=True
                reg1MixerTotal=reg1MixerAmount*reg1MixerPrice
        elif mixerChoice=="3":
            reg2MixerAmount=inputFloatLow("\nHow many would you like to purchase\t",0)
            if reg2MixerAmount!=int(reg2MixerAmount):
                print("Please enter a valid float integer value")
                reg2MixerAmount=0
                time.sleep(1)
            else:
                reg2Mixer=True
                reg2MixerTotal=reg2MixerAmount*reg2MixerPrice
        elif mixerChoice=="4":
            cRInterfaceAmount=inputFloatLow("\nHow many would you like to purchase\t",0)
            if cRInterfaceAmount!=int(cRInterfaceAmount):
                print("Please enter a valid float integer value")
                reg1MixerAmount=0
                time.sleep(1)
            else:
                cRInterface=True
                cRInterfaceTotal=cRInterfaceAmount*cRInterfacePrice
        elif mixerChoice=="/return":
            choice==""
        else:
            print("\nInvalid input, please try again")
            time.sleep(1)
    elif choice=="d":
        nBTriStandPrice=55
        samTriStandPrice=40
        nBDeskStandPrice=25
        print("Here is our list of microphone stands available to purchase:\n")
        print("1. NozamaBasics Tripod Microphone Stand\t$",nBTriStandPrice)
        print("2. Samuel Tripod Microphone Stand\t$",samTriStandPrice)
        print("3. NozamaBasics Desk Microphone Stand\t$",nBDeskStandPrice)
        print("/return to go back to the main menu.\n")
        standChoice=input("Please enter your choice:\t")
        standChoice=standChoice.strip().lower()
        if standChoice=="1":
            nBTriStandAmount=inputFloatLow("\nHow many would you like to purchase\t",0)
            if nBTriStandAmount!=int(nBTriStandAmount):
                print("Please enter a valid float integer value")
                nBTriStandAmount=0
                time.sleep(1)
            else:
                nBTriStandMixer=True
                nBTriStandTotal=nBTriStandAmount*nBTriStandPrice
        elif standChoice=="2":
            samTriStandAmount=inputFloatLow("\nHow many would you like to purchase\t",0)
            if samTriStandAmount!=int(samTriStandAmount):
                print("Please enter a valid float integer value")
                samTriStandAmount=0
                time.sleep(1)
            else:
                samTriStandMixer=True
                samTriStandTotal=samTriStandAmount*samTriStandPrice
        elif standChoice=="3":
            nBDeskStandAmount=inputFloatLow("\nHow many would you like to purchase\t",0)
            if nBDeskStandAmount!=int(nBDeskStandAmount):
                print("Please enter a valid float integer value")
                nBDeskStandAmount=0
                time.sleep(1)
            else:
                nBDeskStandMixer=True
                nBDeskStandTotal=nBDeskStandAmount*nBDeskStandPrice
        elif standChoice=="/return":
            choice==""
        else:
            print("\nInvalid input, please try again")
            time.sleep(1)
    elif choice=="/checkout":
        if sDMic==True or sCMic==True or nBMic==True or sisMKb==True or mdmMKb==True or sisMixer==True or reg1Mixer==True or reg2Mixer==True or cRInterface==True or nBTriStand==True or samTriStand==True or nBDeskStand==True: #the if and else here chose whether to go through with the checkout or notify the user that he has no items in his cart
            clearOrder=input("Would you like to clear your order? (y/n)\t")
            if clearOrder=="y":
                clearOrder=input("Are you sure you want to clear your order and restart? (y/n)\t")
                if clearOrder=="y": #Used to reset all the checkout values in order to clear the cart 
                    sDMic=""
                    sCMic=""
                    nBMic=""
                    sisMKb=""
                    mdmMKb=""
                    sisMixer=""
                    reg1Mixer=""
                    reg2Mixer=""
                    cRInterface=""
                    nBTriStand=""
                    samTriStand=""
                    nBDeskStand=""
                    sDMicTotal=0
                    sCMicTotal=0
                    nBMicTotal=0
                    sisMKbTotal=0
                    mdmMKbTotal=0
                    sisMixerTotal=0
                    reg1MixerTotal=0
                    reg2MixerTotal=0
                    cRInterfaceTotal=0
                    nBTriStandTotal=0
                    samTriStandTotal=0
                    nBDeskStandTotal=0
                    discount=False
                    choice=""
            else:
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
                print("These are the items in your cart\n")
                if sDMic==True: #these if statements make sure that only the items that are bought are displayed
                    print(sDMicAmount,"x\tSure Dynamic Microphone $",sDMicPrice) #these lines print the amount of the same item and its individual price
                if sCMic==True:
                    print(sCMicAmount,"x\tSure Condenser Microphone $",sCMicPrice)
                if nBMic==True:
                    print(nBMicAmount,"x\tSure Condenser Microphone $",nBMicPrice)
                if sisMKb==True:
                    print(sisMKbAmount,"x\tSisela MIDI Keyboard $",sisMKbPrice)
                if mdmMKb==True:
                    print(mdmMKbAmount,"x\tmidiminus MIDI Keyboard $",mdmMKbPrice)
                if sisMixer==True:
                    print(sisMixerAmount,"x\tSisela Audio Mixer (4-Channel 2-Bus) $",sisMixerPrice)
                if reg1Mixer==True:
                    print(reg1MixerAmount,"x\tRegnirheb Audio Mixer (10-Channel 2-Bus) $",reg1MixerPrice)
                if reg2Mixer==True:
                    print(reg2MixerAmount,"x\tRegnirheb Audio Mixer (5-Channel 1-Bus) $",reg2MixerPrice)
                if cRInterface==True:
                    print(cRInterfaceAmount,"x\tConcentrateRight Audio Interface (1-Bus) $",cRInterfacePrice)
                if nBTriStand==True:
                    print(nBTriStandAmount,"x\tNozamaBasics Tripod Microphone Stand $",nBTriStandPrice)
                if samTriStand==True:
                    print(samTriStandAmount,"x\tSamuel Tripod Microphone Stand $",samTriStandPrice)
                if nBDeskStand==True:
                    print(nBDeskStandAmount,"x\tNozamaBasics Desk Microphone Stand $",nBDeskStandPrice)
                priceBeforeDiscount=sDMicTotal+sCMicTotal+nBMicTotal+sisMKbTotal+mdmMKbTotal+sisMixerTotal+reg1MixerTotal+reg2MixerTotal+cRInterfaceTotal+nBTriStandTotal+samTriStandTotal+nBDeskStandTotal
                priceAfterDiscount=priceBeforeDiscount*0.95
                if discount==True:
                    print("Your total without the discount is $",priceBeforeDiscount)
                    print("Discount = -5%")
                    print("\nYour total is $",priceAfterDiscount)
                else:
                    print("\nYour total is $",priceBeforeDiscount)
                paymentComplete=False
                while paymentComplete==False:
                    time.sleep(2)
                    print("How would you like to pay?")
                    print("a. Paypal")
                    print("b. Credit Card")
                    paychoice=input("Your choice:\t")
                    if paychoice=="a":
                        paypalEmail=input("Email: ")
                        paypalPassword=input("Password: ")
                        print("Payment Successful!\nThank you for shopping at Canada's DJs Online Store")
                        paymentComplete=True
                    elif paychoice=="b":
                        ccNumber=input("Credit Card Number: (i hope i dont have to say this but PLEASE DONT actually enter it)")
                        ccExpiryDate=input("Expiry Date: ")
                        ccCVV=input("CVV (on the back of the card): ")
                        print("Payment Successful!\nThank you for shopping at Canada's DJs Online Store")
                        paymentComplete=True
                    else:
                        print("Invalid input, please select a proper payment method")
        else:
            print("Your cart is empty :(")
            time.sleep(2)
            choice=""
    else:
        print("Invalid input, please try again.")
        time.sleep(1)