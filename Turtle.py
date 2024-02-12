# Turtle Game - Pierre Kostantine - December 19, 2022
# This code runs a visual turtle game in which a turtle moves to try and find the lettuce. 
# The user inputs WASD commands to help the turtle.


import random
import time
from Functions import *

# Defines the grid size
gridWidth = 11
gridHeight = 11

# Creates the turtle and lettuce objects
turtleX = 6
turtleY = 5
lettuceX = random.randint(2,10)
lettuceY = random.randint(2,10)

# Defines the movement functions
def moveTurtleUp():
    global turtleY
    if turtleY > 0:
        turtleY -= 1

def moveTurtleDown():
    global turtleY
    if turtleY < gridHeight - 1:
        turtleY += 1

def moveTurtleLeft():
    global turtleX
    if turtleX > 0:
        turtleX -= 1

def moveTurtleRight():
    global turtleX
    if turtleX < gridWidth - 1:
        turtleX += 1

# Creates the game loop
while True:
    grid = []
    for i in range(gridHeight):
        grid.append(["\n"])
        for j in range(gridWidth):
            grid[i].append("\033[36m ▢ ")
    # Updates the grid
    # grid[turtleY][turtleX] = ("\033[1;32mT")
    grid[turtleY][turtleX] = ("🐢 ")
    # The following line can be uncommented to test out how the game would react to different movements
    # grid[lettuceY][lettuceX] = "L"

    # Draws the grid
    for row in grid:
        print(" ".join(row))
    
    oldX=turtleX
    oldY=turtleY

    # Asks the user for a valid key press to move the turtle
    moveTurtle = fourOptionInput("\nEnter a WASD key to move the turtle:\t","w","a","s","d")
    if moveTurtle == "w":
        moveTurtleUp()
    elif moveTurtle == "a":
        moveTurtleLeft()
    elif moveTurtle == "s":
        moveTurtleDown()
    elif moveTurtle == "d":
        moveTurtleRight()
    
    # Calculates distances
    # The abs() function makes sure the value is positive
    oldDistX=abs(lettuceX-oldX)
    oldDistY=abs(lettuceY-oldY)
    newDistX=abs(lettuceX-turtleX)
    newDistY=abs(lettuceY-turtleY)

    # Gives hints and ends the game respectively
    if turtleX==lettuceX and turtleY==lettuceY:
        print('''\033[1;32m
Congratulations!
You helped the turtle find the lettuce!


                             ___-------___ 
                         _-~~             ~~-_ 
                      _-~                    /~-_ 
   /^\__/^\         /~  \                   /    \\ 
 /|  O|| O|        /      \_______________/        \\ 
| |___||__|      /       /                \          \\ 
|          \    /      /                    \          \\ 
|   (_______) /______/                        \_________ \\ 
|         / /         \                      /            \\ 
 \         \^\\         \                  /               \     / 
   \         ||           \______________/      _-_       //\__// 
     \       ||------_-~~-_ ------------- \ --/~   ~\    || __/ 
       ~-----||====/~     |==================|       |/~~~~~ 
        (_(__/  ./     /                    \_\      \. 
               (_(___/                         \_____)_)''')
        break
    elif newDistX<oldDistX or newDistY<oldDistY:
        time.sleep(0.2)
        print("\nThe smell of the lettuce is getting stronger...\n")
        time.sleep(0.7)
        continue
    elif newDistX>oldDistX or newDistY>oldDistY:
        time.sleep(0.2)
        print("\nThe smell of the lettuce is getting weaker...\n")
        time.sleep(0.7)
        continue
    

