year= int(input("Enter the year(Leap year checker): "  ))
#3 steps checking , first the year have to %4 ==0. Second, the year have to % 100 ==0, last the year have to % 400==0
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
