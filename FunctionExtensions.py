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
    option1=option1.strip().lower()
    option2=option2.strip().lower()
    while invalidInput:
        result=input(message)
        if result==option1 or result==option2:
            invalidInput=False
        else:
            print("Please enter a valid choice")
    return result

def threeOptionInput(message,option1,option2,option3):
    invalidInput=True
    option1=option1.strip().lower()
    option2=option2.strip().lower()
    option3=option3.strip().lower()
    while invalidInput:
        result=input(message)
        if result==option1 or result==option2 or result==option3:
            invalidInput=False
        else:
            print("Please enter a valid choice")
    return result

def fourOptionInput(message,option1,option2,option3,option4):
    invalidInput=True
    option1=option1.strip().lower()
    option2=option2.strip().lower()
    option3=option3.strip().lower()
    option4=option4.strip().lower()
    while invalidInput:
        result=input(message)
        if result==option1 or result==option2 or result==option3 or result==option4:
            invalidInput=False
        else:
            print("Please enter a valid choice")
    return result

def fiveOptionInput(message,option1,option2,option3,option4,option5):
    invalidInput=True
    option1=option1.strip().lower()
    option2=option2.strip().lower()
    option3=option3.strip().lower()
    option4=option4.strip().lower()
    option5=option5.strip().lower()
    while invalidInput:
        result=input(message)
        if result==option1 or result==option2 or result==option3 or result==option4 or result==option5:
            invalidInput=False
        else:
            print("Please enter a valid choice")
    return result