# Pig Latin - Pierre Kostantine - Jan 12,2023

# This code is converting a given sentence to pig latin using a while loop and if-else conditions.
# It first defines a set of vowels and then prompts the user to input a sentence.
# The input sentence is first converted to upper case, then split into a list of words.
# The code then iterates through each word, finds the index of the first vowel, and applies the pig latin conversion rules accordingly.
# The pig latin version of the words are added to a list and then joined to form a pig latin sentence.
# Finally, the user is prompted to input another sentence and the process is repeated until the user chooses to exit.
# The function twoOptionInput is imported from another module called Functions and is used to get the input whether to continue or not.

from Functions import *

def main():
    # define the vowels
    VOWELS = "AEIOU"
    ans = "y"
    # Allow multiple cases.
    while ans == "y":
        # input sentence
        mystr = input("Enter a sentence.\t")
        # converting the sentence to upper case
        mystr=mystr.upper()
        # splitting the sentence into words
        words = mystr.split()
        # empty list to store pig latin words
        pig_latin_sentence = []
        # iterating through each word
        for word in words:
            index = 0
            # finding the index of first vowel
            while index < len(word) and (not word[index] in VOWELS):
                index = index+1
            # checking the conditions for pig latin conversion
            if index == 0:
                pig_latin_word = word+"WAY"
            elif index < len(word):
                pig_latin_word = word[index:]+word[:index]+"AY"
            else:
                pig_latin_word = word
            # appending the converted word to pig latin sentence
            pig_latin_sentence.append(pig_latin_word)
        # printing the pig latin sentence
        print(" ".join(pig_latin_sentence))
        # getting the input whether to continue or not
        ans = twoOptionInput("would you like to input another sentence?(y/n)\t","y","n")
        if ans=="y":
            continue
        elif ans=="n":
            break
# calling main function
main()
