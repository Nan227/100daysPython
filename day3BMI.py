#Greeting with user
print("Welcome to the Body Mass Index app")
#User input weight(pound) and height(feet)
weight = float(input("Enter your weight(pound): "))
height = float(input("Enter your height(feet): "))

#convert weight(pounds) to kilograms by division with 2.2
#Covert  height(feet) to meters (1 foot= 0.3048)
weightKM = weight/2.2
heightM = height * 0.3048

#Calculate the BMI
bmi = weightKM/(heightM**2)
bmi = round(bmi,2)

#If BMI is under 18.5, they are Underweight
#If 18.5 < BMI < 25, they are normal weight
#If 25 < BMI < 30, they are overweight
#If 30 < BMI < 35, they are obese
#If Above 35, they are clinically obese
if bmi < 18.5:
  print(f" Your BMI is {bmi} and you are underweight")
elif (bmi >= 18.5) and (bmi < 25):
  print(f" Your BMI is {bmi}, and you are normalweight")
elif (bmi >= 25) and (bmi < 30):
  print(f" Your BMI is {bmi}, and you are overweight")
elif (bmi >= 30) and (bmi < 35):
  print(f" Your BMI is {bmi}, and you are obese")
else:
  print(f" Your BMI is {bmi}, and you are clinically obese")