year= float(input("Enter the year(Leap year checker): "  ))
#3 steps checking , first the year have to %4 ==0. Second, the year have to % 100 ==0, last the year have to % 400==0
if year %4 == 0:
  if year % 100 ==0:
    if year %400 == 0:
       print(f" Year {round(year,0)} is the leap year")
    else:
          print(f" Year {round(year,0)} is not the leap year")
  else:
    print(f" Year {round(year,0)} is the leap year")
else:
  print(f" Year {round(year,0)} is not the leap year")
