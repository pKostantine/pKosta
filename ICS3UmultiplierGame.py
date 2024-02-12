# Dice Rolling Game - Pierre Kostantine - January 9, 2023

# An amusement park is looking for ways to entertain its guests while they wait in line for a very popular ride.
# They have an idea in mind for a game that could be played while people wait and would like to hire you to create the software for the game. 
# The game will have the player earn points which can then be traded in for a prize after the ride has finished.
# The player starts the game with an “account” with 0 points in it.
# The game consists of 5 rounds of play where the amount of points earned from each round is added to the account.
# After the 5 rounds are over the player can withdraw all of the points in his account


from Functions import * #Used this to connect to the second file: Extensions.py
import random #Used this to retrieve random values
import math #Used for math
import time #Used this for making the GUI cleaner by putting delays in between different menus and reponses
import sys #Used this to end the system when program finished

accPoints=0
roundNumber=0
aAmount=0
bAmount=0
cAmount=0
dAmount=0
eAmount=0
fAmount=0
gAmount=0
a=False
b=False
c=False
d=False
e=False
f=False
g=False

print('''
               ☥ Welcome to AnkhLand ☥

                .,aadd"'    `"bbaa,. 
            ,ad8888P'          `Y8888ba, 
         ,a88888888              88888888a, 
       a88888888888              88888888888a 
     a8888888888888b,          ,d8888888888888a 
    d8888888888888888b,_    _,d8888888888888888b 
   d88888888888888888888888888888888888888888888b 
  d8888888888888888888888888888888888888888888888b 
 I888888888888888888888888888888888888888888888888I 
,88888888888888888888888888888888888888888888888888, 
I8888888888888888PY8888888PY88888888888888888888888I 
8888888888888888"  "88888"  "88888888888888888888888 
8::::::::::::::'    `:::'    `:::::::::::::::::::::8 
Ib:::::::::::"        "        `::::::' `:::::::::dI 
`8888888888P            Y88888888888P     Y88888888' 
 Ib:::::::'              `:::::::::'       `:::::dI 
  Yb::::"                  ":::::"           "::dP 
   Y88P                      Y8P               `P 
    Y'                        " 
                                `:::::::::::;8" 
       "888888888888888888888888888888888888" 
         `"8;::::::::::::::::::::::::::;8"' 
            `"Ya;::::::::::::::::::;aP"' 
                ``""YYbbaaaaddPP""''\n\n''')

time.sleep(2)
accName=input("What is your name?\t")
accName=accName.capitalize()

print("Hey ",accName,"\b! While you wait in line, we have a game for you.")
time.sleep(1)

instructionsChoice=twoOptionInput("Would you like to see the instructions? (y/n)\t","y","n")
if instructionsChoice=="y":
    print('''==============================================================================================================================
                                           .d88b.        INSTRUCTIONS 
                                           88  88                              _______ 
                                           `8bd8'                             /\ o o o\ 
                                            `88'                             /o \ o o o\_______
                                        g888SEAL888g                        <    >------>   o /|
                                             88                              \ o/  o   /_____/o|
                                             88                               \/______/     |oo|
                                             88                                     |   o   |o/
                                            d88b                                    |_______|/
                                           d8888b     \n''')
    print("The game will have you earn points which can then be traded in for a prize after the ride has finished.")
    time.sleep(4)
    print("The game consists of 5 rounds of play where the amount of points earned from each round is added to your account.")
    time.sleep(6)
    print("After the 5 rounds are over you can withdraw all of the points in your account")
    time.sleep(3)
    print("______________________________________________________________________________________________________________________________\n\t\t\t\t\t\tHow to play each round:\n")
    print("You will roll two dice. One dice has 9 sides the other dice has 6 sides.")
    time.sleep(4)
    print("You can roll the dice as many times as you wish during a round and can “bank” your points to your account at any time you\nwant, thus starting a new round.")
    time.sleep(7)
    print("There are however both incentives and punishments for rolling the dice too many times.")
    time.sleep(4)
    print("______________________________________________________________________________________________________________________________\n\t\t\t\t\t\tIncentives to Rolling:\n")
    print("If you bank to your account a total of at least 50 points in a single round, you will double the points that sit in the\naccount after the round is complete")
    time.sleep(8)
    print("If you bank to your account a total of at least 75 points in a single round, you will triple the points that sit in the\naccount after the round is complete")
    time.sleep(7)
    print("If you bank to your account a total of at least 100 points in a single round, you will quadruple the points that sit in\nthe account after the round is complete")
    time.sleep(7)
    print("If you roll double 6’s at least 5 times in a single round, you will increase the points that sit in the account after the\nround is complete by 20 times")
    time.sleep(7)
    print("______________________________________________________________________________________________________________________________\n\t\t\t\t\t\tPunishments to Rolling:\n")
    print("If you roll a 1 on either dice at any point during the round your total points for the round get reset to zero\n(You can keep rolling in the round)")
    time.sleep(8)
    print("If you roll a sum of 7 then the amount of points you currently have in the round is cut in half (round up)\n(You can keep rolling in the round)")
    time.sleep(7)
    print('''If you roll a snake eyes (Both dice show 1) at any point during the round your total points for the round get
reset to zero and your account balance gets reset to zero. (You can keep rolling in the round)  / . .\ 
                                                                                                \  ---<
                                                                                                 \  /
                                                                                       __________/ /
                                                                                    -_:___________/''')
    print("\n==============================================================================================================================")
    time.sleep(9)
    print("Let's begin!")

while roundNumber<5:
    roundNumber+=1
    roundPoints=0
    turnPoints=0
    double6=0
    print("\n==============================================================================================================================\n\t\t\t\t\t\tROUND ",roundNumber)
    firstRoll=True
    while True:
        # check if it's the first roll of the round
        if firstRoll==True:
            firstRoll=False
            roll="y"
        else:
            print("\n______________________________________________________________________________________________________________________________\n")
            roll=twoOptionInput("Would you like to  keep rolling? (y/n)\t","y","n")
        if roll=="y":
            dice1=random.randint(1,9)
            dice2=random.randint(1,6)
            turnPoints=dice1+dice2
            roundPoints+=turnPoints
            # check if the player rolled a double 6
            if dice1==6 and dice2==6:
                double6+=1
            # check if the player rolled a 1 on either dice
            if dice1==1 or dice2==1:
                turnPoints=0
                roundPoints=0
            # check if the player rolled a 7
            if dice1+dice2==7:
                roundPoints/=2
                roundPoints=int(roundPoints)
            # check if the player rolled a pair of 1s
            if dice1==1 and dice2==1:
                print('''
                            __..._              
                        ..-'      o.            
                     .-'            :           
                 _..'             .'__..--<     
          ...--""                 '-.           
      ..-"                       __.'           
    .'                  ___...--'               
   :        ____....---'                        
  :       .'                                    
 :       :           _____                      
 :      :    _..--"""     """--..__             
:       :  ."                      ""i--.       
:       '.:                         :    '.     
:         '--...___i---""""--..___.'      :     
 :                 ""---...---""          :     
  '.                                     :      
    '-.                                 :       
       '--...                         .'        
         :   ""---....._____.....---""          
         '.    '.                               
           '-..  '.                             
               '.  :                            
                : .'                            
               /  :                             
             .'   :                             
           .' .--'                              
          '--'

You rolled a SNAKES EYE!!!''')
                turnPoints=0
                roundPoints=0
                accPoints=0
            time.sleep(2)
            # print the current results after each roll
            print("You rolled a",dice1,"and a",dice2,"\nYou scored",turnPoints,"points this turn.\nYou have",roundPoints,"points this round\nYou have",accPoints,"points in your account.")
            continue
        elif roll=="n":
            if roundPoints>=50 and roundPoints<75:
                roundPoints*=2
            elif roundPoints>75 and roundPoints<100:
                roundPoints*=3
            elif roundPoints>100:
                roundPoints*=4
            if double6>=6:
                roundPoints*=20
            print("You have",roundPoints,"points this round.\nYou have",accPoints,"points in your account.")
            accPoints+=roundPoints
            print("\n==============================================================================================================================")
            time.sleep(2)
            break

print('''
                   ☥ Welcome to AnkhLand's Prize Store ☥ 
                                    \  / 
                                    (()) 
                                    ,~L_ 
                                   2~~ <\ 
                                   )>-\y(((GSSSSSSssssss>=_/ 
 ___________________________________)v_\__________________________________ 
(_// / / / (///////\3__________((_/      _((__________E/\\\\\\\\\\\\\\) \ \ \ \\\\_) 
  (_/ / / / (////////////////////(c  (c /|\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\) \ \ \ \_) 
    "(_/ / / /(/(/(/(/(/(/(/(/(/(/\_    /\)\)\)\)\)\)\)\)\)\)\ \ \ \_)" 
       "(_/ / / / / / / / / / / / /|___/\ \ \ \ \ \ \ \ \ \ \ \ \_)" 
          "(_(_(_(_(_(_(_(_(_(_(_(_[_]_|_)_)_)_)_)_)_)_)_)_)_)_)" 
                                   |    \ 
                                  /      | 
                                 / /    /___ 
                                /           "~~~~~__ 
                                \_\_______________\_"_? ''')

#initialize starting account points and item prices
ogAccPoints=accPoints
aPrice=1500
bPrice=500
cPrice=400
dPrice=200
ePrice=100
fPrice=50
gPrice=25

while True:
    print("Points:",int(accPoints))
    print('''
Here is the list of items available to purchase:

a.      Nefertiti Life-Sized Statue (1500 Points)
b.      Snake Eyes Statue           (500 Points)
c.      Nefertiti Statue            (400 Points)
d.      Snake Eyes Large Keychain   (200 Points)
e.      Pocket Aankh                (100 Points)
f.      Ankh Keychain               (50 Points)
g.      Pyramids Keychain           (25 Points)
h.      Cart''')
    # Prompt user to select item to purchase
    buyChoice=eightOptionInput("What would you like to purchase?\t","a","b","c","d","e","f","g","h")
    purchaseMessage="How many would you like to purchase?\t"
    # Check if user select item 'a'
    if buyChoice=="a":
        a=True
        aAmount+=checkout(purchaseMessage,aPrice,0,accPoints,"Nefertiti Life-Sized Statue")
        accPoints-=aPrice*aAmount
        continue
    # Check if user select item 'b'
    elif buyChoice=="b":
        b=True
        bAmount+=checkout(purchaseMessage,bPrice,0,accPoints,"Snake Eyes Statue")
        accPoints-=bPrice*bAmount
        continue
    # Check if user select item 'c'
    elif buyChoice=="c":
        c=True
        cAmount+=checkout(purchaseMessage,cPrice,0,accPoints,"Snake Eyes Statue")
        accPoints-=cPrice*cAmount
        continue
    # Check if user select item 'd'
    elif buyChoice=="d":
        d=True
        dAmount+=checkout(purchaseMessage,dPrice,0,accPoints,"Nefertiti Statue")
        accPoints-=dPrice*dAmount
        continue
    # Check if user select item 'e'
    elif buyChoice=="e":
        e=True
        eAmount+=checkout(purchaseMessage,ePrice,0,accPoints,"Snake Eyes Large Keychain")
        accPoints=accPoints-ePrice*eAmount
        continue
    # Check if user select item 'f'
    elif buyChoice=="f":
        f=True
        fAmount+=checkout(purchaseMessage,fPrice,0,accPoints,"Ankh Keychain")
        accPoints=accPoints-fPrice*fAmount
        continue
    # Check if user select item 'g'
    elif buyChoice=="g":
        g=True
        gAmount+=checkout(purchaseMessage,gPrice,0,accPoints,"Pyramids Keychain")
        accPoints=accPoints-gPrice*gAmount
        continue
    # Check if user select item 'h'
    elif buyChoice=="h":
        cart=threeOptionInput("a.\tCheckout\nb.\tClear Order\nc.\tContinue Shopping\n","a","b","c")
        if cart=="a":
            if aAmount==0:
                a=False
            elif bAmount==0:
                b=False
            elif cAmount==0:
                c=False
            elif dAmount==0:
                d=False
            elif eAmount==0:
                e=False
            elif fAmount==0:
                f=False
            elif gAmount==0:
                g=False
            print("These are the items in your cart\n")
            if a==True: #these if statements make sure that only the items that are bought are displayed
                print(aAmount,"x\tNefertiti Life-Sized Statue\t",aPrice,"Points") #these lines print the amount of the same item and its individual price
            if b==True:
                print(bAmount,"x\tSnake Eyes Statue\t\t",bPrice,"Points")
            if c==True:
                print(cAmount,"x\tNefertiti Statue\t\t",cPrice,"Points")
            if d==True:
                print(dAmount,"x\tSnake Eyes Large Keychain\t",dPrice,"Points")
            if e==True:
                print(eAmount,"x\tPocket Aankh\t\t\t",ePrice,"Points")
            if f==True:
                print(fAmount,"x\tAnkh Keychain\t\t\t",fPrice,"Points")
            if g==True:
                print(gAmount,"x\tPyramids Keychain\t\t",gPrice,"Points")
            if a!=True and b!=True and c!=True and d!=True and e!=True and f!=True and g!=True:
                emptyCartCheckout=twoOptionInput("Your cart is currently empty. Are you sure you want to leave? (y/n)\t","y","n")
                if emptyCartCheckout=="y":
                    print("Thank you for playing this game, goodbye!")
                    sys.exit()
                elif emptyCartCheckout=="n":
                    continue
            total=aAmount*aPrice+bAmount*bPrice+cAmount*cPrice+dAmount*dPrice+eAmount*ePrice+fAmount*fPrice+gAmount*gPrice
            print("Your total is:\t",total,"Points")
            time.sleep(3)
            print("Congratulations and thank you for playing this game, goodbye!")
            sys.exit()
        elif cart=="b":
            a=False
            b=False
            c=False
            d=False
            e=False
            f=False
            g=False
            aAmount=0
            bAmount=0
            cAmount=0
            dAmount=0
            eAmount=0
            fAmount=0
            gAmount=0
            accPoints=ogAccPoints
        elif cart=="c":
            continue