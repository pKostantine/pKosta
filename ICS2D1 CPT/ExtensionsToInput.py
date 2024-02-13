def isFloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def inputFloat(message):
    invalidInput=True
    while invalidInput:
        result=input(message)
        if isFloat(result):
            result=float(result)
            invalidInput=False
        else:
            print("Please enter a valid float value")
    return result

def inputFloatLow(message,lowBound):
    invalidInput=True
    while invalidInput:
        result=inputFloat(message)
        if result<=lowBound:
            print("Please enter a value larger than ",lowBound)
        else:
            invalidInput=False
    return result
