import random

print("Who will pay the bill today? ")
name = input("Enter lucky names today: ")
nameSlit = name.split(" ")
print(nameSlit)
numName=len(nameSlit)
random_name = random.randint(0, numName-1)
print(f"{nameSlit[random_name]} is a rich person \n and {nameSlit[random_name]} will pay the bill today ")
