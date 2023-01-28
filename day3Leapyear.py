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