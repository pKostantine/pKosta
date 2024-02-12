#This file is copied into every program and is an extension to my inputs

def isFloat(string): #makes sure the variable is a valid float value
    try:
        float(string)
        return True
    except ValueError:
        return False

def inputFloat(message): #makes sure the user input is a valid float value
    invalidInput=True
    while invalidInput:
        result=input(message)
        if isFloat(result):
            result=float(result)
            invalidInput=False
        else:
            print("Please enter a valid float value")
    return result

def isInt(string): #makes sure the variable is a valid float value
    try:
        int(string)
        return True
    except ValueError:
        return False

def inputInt(message): #makes sure the user input is a valid float value
    invalidInput=True
    while invalidInput:
        result=input(message)
        if isInt(result):
            result=int(result)
            invalidInput=False
        else:
            print("Please enter a valid integer value")
    return result

def inputFloatLow(message,lowBound): #makes sure the user input is a valid float value larger than a specific value
    invalidInput=True
    while invalidInput:
        result=inputFloat(message)
        if result<=lowBound:
            print("Please enter a value larger than ",lowBound)
        else:
            invalidInput=False
    return result

def inputFloatHigh(message,highBound): #makes sure the user input is a valid float value smaller than a specific value
    invalidInput=True
    while invalidInput:
        result=inputFloat(message)
        if result>=highBound:
            print("Please enter a value smaller than ",highBound)
        else:
            invalidInput=False
    return result

def inputFloatLowHigh(message,lowBound,highBound): #makes sure the user input is a valid integer value larger than a specific value
    invalidInput=True
    while invalidInput:
        result=inputFloat(message)
        if result<=lowBound or result>=highBound:
            print("Please enter a float value larger than",lowBound,"and less than",highBound)
        else:
            invalidInput=False
    return result

def inputIntLow(message,lowBound): #makes sure the user input is a valid integer value larger than a specific value
    invalidInput=True
    while invalidInput:
        result=inputFloat(message)
        if result<=lowBound or result!=int(result):
            print("Please enter an integer value larger than ",lowBound)
        else:
            invalidInput=False
    return result
    
def inputIntHigh(message,highBound): #makes sure the user input is a valid integer value smaller than a specific value
    invalidInput=True
    while invalidInput:
        result=inputFloat(message)
        if result>=highBound or result!=int(result):
            print("Please enter an integer value smaller than ",highBound)
        else:
            invalidInput=False
    return result

def inputIntLowHigh(message,lowBound,highBound): #makes sure the user input is a valid integer value larger than a specific value
    invalidInput=True
    while invalidInput:
        result=inputFloat(message)
        if result<=lowBound or result>=highBound or result!=int(result):
            print("Please enter an integer value larger than",lowBound,"and less than",highBound)
        else:
            invalidInput=False
    return result

def twoOptionInput(message,option1,option2):
    invalidInput=True
    while invalidInput:
        result=input(message)
        result=result.strip().lower()
        if result==option1 or result==option2:
            invalidInput=False
        else:
            print("Please enter a valid choice")
    return result

def threeOptionInput(message,option1,option2,option3):
    invalidInput=True
    while invalidInput:
        result=input(message)
        result=result.strip().lower()
        if result==option1 or result==option2 or result==option3:
            invalidInput=False
        else:
            print("Please enter a valid choice")
    return result

def fourOptionInput(message,option1,option2,option3,option4):
    invalidInput=True
    while invalidInput:
        result=input(message)
        result=result.strip().lower()
        if result==option1 or result==option2 or result==option3 or result==option4:
            invalidInput=False
        else:
            print("Please enter a valid choice")
    return result

def fiveOptionInput(message,option1,option2,option3,option4,option5):
    invalidInput=True
    while invalidInput:
        result=input(message)
        result=result.strip().lower()
        if result==option1 or result==option2 or result==option3 or result==option4 or result==option5:
            invalidInput=False
        else:
            print("Please enter a valid choice")
    return result

def eightOptionInput(message,option1,option2,option3,option4,option5,option6,option7,option8):
    invalidInput=True
    while invalidInput:
        result=input(message)
        result=result.strip().lower()
        if result==option1 or result==option2 or result==option3 or result==option4 or result==option5 or result==option6 or result==option7 or result==option8:
            invalidInput=False
        else:
            print("Please enter a valid choice")
    return result    

def checkout(message,price,lowBound,highBound,itemName):
    while True:
        result=inputInt(message)
        amountTest=result*price
        if highBound<price:
            print("You do not have sufficient funds to purchase this item")
            result=0
            break
        elif amountTest<lowBound or amountTest>highBound or amountTest!=int(amountTest):
            print("Please enter an integer value larger than",lowBound,"and less than the amount of points in your account")
            continue
        else:
            print("Added",result,"\b",itemName,"to cart!")
            break
    return result