year= float(input("Enter the year(Leap year checker): "  ))
#3 steps checking , first the year have to %4 ==0. Second, the year have to % 100 ==0, last the year have to % 400==0
if year %4 == 0:
  if year % 100 ==0:
    if year %400 == 0:
       print(f" Year {round(year,0)} is the leap year")
year= int(input("Enter the year(Leap year checker): "  ))
#3 steps checking , first must %4 ==0. Second, must % 100 !=0, last must % 400==0
yearF=float(year)
if yearF %4 == 0:
  if yearF % 100 ==0:
    if yearF %400 == 0:
       print(f" Year {year} is the leap year")
    else:
          print(f" Year {year} is not the leap year")
  else:
    print(f" Year {year} is the leap year")
else:
  print(f" Year {year} is not the leap year")
