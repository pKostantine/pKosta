# Emilia Numbers - Pierre Kostantine - Jan 13, 2023

# Program that finds Emilia Numbers, and then use it to count how many Emilia numbers would you find for the numbers from 1 to 1000

def isEmilia(number):
    factorList = []
    # Create a list of factors of the number
    for i in range(1, number + 1):
        if number % i == 0:
            factorList.append(i)
            # Iterate over the list of factors, comparing the sum of one pair with the difference of another pair
    for x in factorList:
        for y in factorList:
            if x + y == (number//x) - (number//y):
                return True
    return False

def getEmiliaNumbers(min, max):
    if max <= 10000:
        emiliaList = []
        # Iterate over the range from min to max, checking if each number is an Emilia number
        for i in range(min, max + 1):
            if isEmilia(i):
                emiliaList.append(i)
        return emiliaList
    else:
        return -1

# Print the number of Emilia numbers found, and the list of Emilia numbers
emiliaNumbers = getEmiliaNumbers(1, 1000)
print("Number of Emilia numbers from 1 to 1000:", len(emiliaNumbers))
print("Emilia numbers from 1 to 1000:", emiliaNumbers)