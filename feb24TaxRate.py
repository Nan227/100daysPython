# def abs(x):
#   if x <0:
#     absx = -x
#     print("Flipped")
#   else:
#     absx = x
#     print("Same")
#   return absx
# print("After that")
# print(abs(-555))
# #### case 2
# def abs(y):
#   if y<0:
#     return -y
#   else:
#     return y
# print(abs(-332))
income=int(input("Enter your income: "))
def taxrate(income):
  if income <= 33000:
    taxrate = 0.21
    tax=income*0.21
  else:
    if income <= 67000:
      taxrate = 0.24
      tax=((income-33000)*0.24)+(33000*0.21)
    else: 
      if income <= 94000:
        taxrate = 0.27
        tax=((income-67000)*0.27)+((67000-33000)*0.24)+(33000*0.21)
      else:
        if income <= 176000:
          taxrate = 0.31
          tax=((income-94000)*0.31)+((176000-94000)*0.27)+((67000-33000)*0.24)+(33000*0.21)
        else:
          taxrate = 0.35
          tax=((income-176000)*0.35)+((176000-94000)*0.31)+((176000-94000)*0.27)+((67000-33000)*0.24)+(33000*0.21)
  return(tax)
  
#print(taxrate(income))
print(f"Your income is ${income} and you will pay tax ${taxrate(income)} this year")