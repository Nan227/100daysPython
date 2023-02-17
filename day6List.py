classmade = ["Nan", "Larry","Jamie","Bogda"]
for i in classmade:
  print(i)
print("-----------------------------------")
student_heights = input("Input student hights then , :")
for n in range(0, len(student_heights)):
  highSlit = student_heights.split(",")
  # student_heights[n]=int(nameSlit)
print(highSlit)
highSlitInt =int(highSlit)
for i in range(0,len(highSlitInt)):
  totalhigh = highSlitInt[i]+highSlitInt[i+1]
print(totalhigh)
