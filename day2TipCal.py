#Tip-calculator app

# User inputs 3 value ( Cost of the bill, percent of the Taxes, number of people)
print('Welcome to the Tip-Calculator app \n')
bill =input('How much the bill cost? ')
percent = input('How much percentage of Taxes? ')
split = input('How many people split the bill? ')

#convert str => number
billF = float(bill)
percentF = float(percent)
splitI= int(split)

#calculate
totalbill = round(billF + (billF*percentF/100),2)
eachPay = round(totalbill/splitI,2)
print('\nYour total bill is '+ str(totalbill))
print('\nEach person will pay '+ str(eachPay))
