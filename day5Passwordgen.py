import random
import re
letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbol = ['!', '@', '#', '$', '%', '^', '&', '*' ,'(',')','_','+','.']

print("WElcome to the PyPassword Gennerator!")
nr_letters=int(input("How many letters would you like in your password?\n=> "))
nr_symbols=int(input("How many symbols would you like in your password?\n=> "))
nr_numbers=int(input("How many numbers would you like in your password?\n=>"))
k=0
passwordLetter=random.choices(letter, k=nr_letters)
passwordSymbol=random.choices(symbol, k=nr_symbols)
passwordNumbers=random.choices(number, k=nr_numbers)
password=passwordLetter+passwordSymbol+passwordNumbers

random.SystemRandom().shuffle(password)
n=''.join(password)
print(f"You password is {n}")