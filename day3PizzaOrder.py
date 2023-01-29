print("Welcome to LP Pizza \n")
size = input("What size of pizza do you want? S, M, or L: ")
add_pepperoni = input("Do you want to add peperoni?: Y or N: ")
extra_cheese = input("Do you want to add extra cheese?: Y or N: ")
numberOfPizza = input("How many pizza do you want for this order? ")
# calcutator
if size =="S":
  price = 10
elif size =="M":
  price = 12
elif size == "L":
  price =14
 else:
  print("Sorry, you order is errored. Please re-order again")
