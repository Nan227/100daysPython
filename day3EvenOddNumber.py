# User input number
print("Welcome to Even or Odd Number Checker app ")
number = int(input("Which number do you want to check? "))
# check with %
if(number%2)==0:
  print(" Your number is "+ str(number)+ ", it is even number")
elif(number%2)!=0:
  print("\nYour number is "+ str(number)+ ", it is odd number")
else:
  print("The system error ")

