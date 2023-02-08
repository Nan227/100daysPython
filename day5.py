import random

name=input("Enter you classmades' names: ")
nName = name.split(" ")
print(f"Your classmades are: {nName}")
for nameEach in nName:
  print(nameEach + " is grumpy")
numberName = int(len(nName))
print(f"\nYou have {numberName} classmades")

############################################

newfriend = [ "Steve","Jooby","Casy"]
addfriend1 = nName+newfriend
print(addfriend1*3)
print(addfrined1[0])
print(addfrined1[0][1])
####################################

addfriened2 = nName.append(newfriend)
print(addfriened2*3)
print(addfrined2[0])
print(addfrined2[0][1])
###################################

