print("Welcome to LP Pizza \n")
size = input("What size of pizza do you want? S, M, or L: ")
add_pepperoni = input("Do you want to add peperoni?: Y or N: ")
extra_cheese = input("Do you want to add extra cheese?: Y or N: ")
numberOfPizza = int(input("How many pizza do you want for this order? "))
# calcutator
if size =="S":
  if add_pepperoni == "Y":
    if extra_cheese == "Y":
      price = 15+2+1
    else:
      price = 15+2
  else:
    price = 15
elif size =="M":
  if add_pepperoni == "Y":
    if extra_cheese == "Y":
      price = 20+3+1
    else:
      price = 20+3
  else:
    price = 20
elif size =="L":
  if add_pepperoni == "Y":
    if extra_cheese == "Y":
      price = 25+3+2
    else:
      price = 25+3
  else:
    price = 25  


else:
  print("Sorry, you order is errored. Please re-order again")

print(f"\nYou order {size} with {add_pepperoni} peperroni and {extra_cheese} extra cheese ")
print(f"Your price of one pizza is {price}")
totalbill= numberOfPizza*price
print(f"You order {numberOfPizza} , you total bill is {totalbill} ")
