import random

print("Random function")
random_int = random.randint(1,10)
print(random_int)
random_float = random.random()
print(random_float)
print("\n Random Head or Tail game")
random_HT=random.randint(0,2)
if random_HT==0:
  print("Head")
else:
  print("Tail")

