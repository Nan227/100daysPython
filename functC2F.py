#input in Celsius 
celsiusInput=int(input("Enter the Celsius temperature: "))
# function :degC*9/5+32
fahrenheit = celsiusInput*9/5+32
#output in Fahenheit
print(f" Your input {celsiusInput} Celsius  = {fahrenheit} Fahrenheit")

# function
def degf(celsiusInput):
  return celsiusInput*9/5+32

print(f"Confirmed that Your input will convert to: {degf(celsiusInput)} Fahrenheit")

