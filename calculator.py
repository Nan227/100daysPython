# User input 2 number and 1 operator
num1 =float(input("Enter the first number: "))
op = input("Enter the opperator ' +, -, *, / ' : ")
num2 =float(input("Enter the first number: "))

# calculate
if op =="+":
  result = num1 + num2
elif op =="-":
  result = num1 - num2
elif op =="*":
  result = num1 * num2
elif op =="/":
    result = num1 / num2
else: 
    print("No answer is not correct")
print(str(num1)+ " "+ op + " "+ str(num2) + " = "+ str(round(result,2)))
