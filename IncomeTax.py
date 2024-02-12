# Income Tax - Pierre Kostantine

from FunctionExtensions import * #Used this to connect to the second file: Extensions.py
import time

rrspValue=0
charityValue=0
invalidIncomePostFunds=True

income=inputFloatLow("What is your taxable income in Ontario?\n(Please use the full number and do not replace 1000 for \"k\"\t$ ",0)
income=round(income,2)
rrspMax=round(income*1.18,2)
rrsp=twoOptionInput("would you like to input any RRSP funds? (y/n)\t\t\t  ","y","n")
if rrsp=="y":
    rrspValue=inputFloatLowHigh("Enter your RRSP funds.\t\t\t\t\t\t$ ",0,rrspMax)
elif rrsp=="n":
    rrspValue=0
incomePostRRSP=income-rrspValue
charity=twoOptionInput("Would you like to input any charity donations? (y/n)\t\t  ","y","n")
if charity=="y":
    charityValue=inputFloatLowHigh("Please enter your charity donations.\t\t\t\t$ ",0,incomePostRRSP)
elif charity=="n":
    charityValue=0

incomePostFunds=incomePostRRSP-charityValue

if incomePostFunds<=50197:
    fedTax=(incomePostFunds)*0.15
elif incomePostFunds<=100392:
    fedTax=(incomePostFunds-50197)*0.205+7529.55
elif incomePostFunds<=155625:
    fedTax=(incomePostFunds-100392)*0.26+17819.525
elif incomePostFunds<=221708:
    fedTax=(incomePostFunds-155625)*0.29+32180.104
else:
    fedTax=(incomePostFunds-221708)*0.33+51344.174

if incomePostFunds<=46226:
    provTax=incomePostFunds*0.0505
elif incomePostFunds<=92454:
    provTax=(incomePostFunds-46226)*0.0915+2334.413
elif incomePostFunds<=150000:
    provTax=(incomePostFunds-92454)*0.1116+4229.862+2334.413
elif incomePostFunds<=220000:
    provTax=(incomePostFunds-150000)*0.1216+6422.1335+4229.862+2334.413
else:
    provTax=(incomePostFunds-220000)*0.1316+8512+6422.1336+4229.862+2334.413
provTax=round(provTax,2)
fedTax=round(fedTax,2)
netIncome=round(incomePostFunds-fedTax-provTax,2)
if incomePostFunds>0:
    time.sleep(1)
    print("Your total federal tax is\t\t\t\t\t$",fedTax)
    time.sleep(2)
    print("Your total provincial tax is\t\t\t\t\t$",provTax)
    time.sleep(2)
    print("Your net income is\t\t\t\t\t\t$",netIncome)
else:
    print("Sorry there was an error in the calculations, please make sure you input a positive taxable income.\nWe will end the user to system connection, please reload and try again.")