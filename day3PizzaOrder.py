print("Welcome to LP Pizza \n")
size = input("What size of pizza do you want? S, M, or L: ")
add_pepperoni = input("Do you want to add peperoni?: Y or N: ")
extra_cheese = input("Do you want to add extra cheese?: Y or N: ")
numberOfPizza = int(input("How many pizza do you want for this order? "))
# calcutator
if size =="S":
  if add_pepperoni == "Y":
    if extra_cheese == "Y":
      price = 10+2+2
      print(f"You order {size} with {add_pepperoni} peperroni and {extra_cheese} extra cheese ")
    else:
      price = 10+2
      print(f"You order {size} with {add_pepperoni} peperroni and {extra_cheese} extra cheese ")
  else:
    price = 10
    print(f"You order {size} with {add_pepperoni} peperroni and {extra_cheese} extra cheese ")
elif size =="M":
  if add_pepperoni == "Y":
    if extra_cheese == "Y":
      price = 12+2+2
      print(f"You order {size} with {add_pepperoni} peperroni and {extra_cheese} extra cheese ")
    else:
      price = 12+2
      print(f"You order {size} with {add_pepperoni} peperroni and {extra_cheese} extra cheese ")
  else:
    price = 12
    print(f"You order {size} with {add_pepperoni} peperroni and {extra_cheese} extra cheese ")
elif size == "L":
 if add_pepperoni == "Y":
    if extra_cheese == "Y":
      price = 14+2+2
      print(f"You order {size} with {add_pepperoni} peperroni and {extra_cheese} extra cheese ")
    else:
      price = 14+2
      print(f"You order {size} with {add_pepperoni} peperroni and {extra_cheese} extra cheese ")
  else:
    price = 14
    print(f"You order {size} with {add_pepperoni} peperroni and {extra_cheese} extra cheese ")
else:
  print("Sorry, you order is errored. Please re-order again")

totalbill= numberOfPizza*price
print(f"You total bill is {totalbill} ")
