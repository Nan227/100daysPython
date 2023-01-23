# 9:00 hello world program
print("Hello "+ "World")

# 13:00 draw out
print("   /|")
print("  / |")
print(" /  |")
print("/___|")

# 15:00 Data and variable
character_name="Steve"
character_age= "2 "
print("My name is " + character_name)
print("I am " + character_age + "years old")
print("I really like " + character_name + "'s name")
print("I don't like to be "+character_age + " year old")

#working with string \" => print "\"
# .lower(), upper(), isupper(), "phrase.upper().isupper()""
#len(phrase)
phrase="Test test2"
print(len(phrase))
#print(phrase.index(G) => 0
print(phrase.index("t"))

print(phrase.replace("test2", "notest"))
#41:00 number
num = -5
print(type(num)) # cannot print num next to string
print(num)
# print(pow(3,2)) = 9
print("\n pow" )
print(pow(3,2))
# print(abs(-5)) => 5

# round(3.7) => 4

# from math import *
#sqrt(36) => 6

#48:45 getting input

#input("Enter your lucky number ")

# 53:00 input 2 number => basic calculator
#result = num1 + num2

# 59:00 mad lip game
color= input("Input a color ")
celebrity = input("Input your celebrity")
print(celebrity)
print(color)
# list
friends =["Kevin", "Kevon","Kony", "Kiddy" ]
print(friends[1:3]) # Kevon Kony
# .append => add the end of the list
friends.append("Kedo")
print(".append" + str(friends))
# .insert(1, "dd") => put new one
friends.insert(1, "Karen")
print(".insert _1_ Karen"+ str(friends))
# .remove()
friends.remove("Kevin")
print(".remove"+str(friends))
#.pop() => last remove
friends.pop()
print(".pop"+ str(friends))

# frinds.index("kevin") => 0
#frinds.sort() => small => big
#.reverse(), 
#friend2 = friend.copy()

#1:20 tupel
coordinates =(4, 5) #immunible cannot change
print(coordinates[1]) # => 5
#1:24:00 function
def sayhi(name, age): 
  print("Hello " + name + " you are "+ str(age))
sayhi("Mike", "20")
sayhi("Shirley", "15")
#1.34:00 return function
def cube(num):
  return num*num*num
result = cube(4)
print(result)
#1:45:00 
