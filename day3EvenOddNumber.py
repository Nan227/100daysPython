# User input number
print("Welcome to Even or Odd Number Checker app ")
number = int(input("Which number do you want to check? "))
# check with %
if(number%2)==0:
  print(" Your number is "+ str(number)+ ", it is even number")
else:
  print("\nYour number is "+ str(number)+ ", it is odd number")

print("\nWelcome to roller coaster ride")
print("This machine is allowed people who is higher than 120cm to play")
high = float(input("How tall are you? "))
if high >=120:
  age= int(input("How old are you? "))
  if age>=45 and age<=55:
    print("Cost of a ride roller coaster is $0")
  elif age >18:
    print("Cost of a ride roller coaster is $12")
  else:
    print("Cost of a ride roller coaster is $7")
else:
  print("Sorry, you can not play the roller coaster at this time")

