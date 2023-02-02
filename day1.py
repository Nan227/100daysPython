#docs.python.org
print("Welcome to factorial calculator ")
n = int(input("Enter the factorial number: "))                  # Reading input from STDIN
fac=1

for i in range(1,n+1):
  fac = fac*i

print(f"You enter the factorial of {n} = {fac}") 

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
dirty_dozen = [fruits, vegetables]
 
print(dirty_dozen[1][2])

