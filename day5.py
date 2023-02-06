import random

name=input("Enter you classmades' names: ")
nName = name.split(" ")
print(f"Your classmades are: {nName}")
for nameEach in nName:
  print(nameEach + " is grumpy")
numberName = int(len(nName))
print(f"\nYou have {numberName} classmades")
