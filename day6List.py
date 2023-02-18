classmade = ["Nan", "Larry","Jamie","Bogda"]
for i in classmade:
  print(i)
print("-----------------------------------")
student_heights = input("Input student hights: ").split()
#for n in range(0, len(student_heights)):
  #student_heights[n]=int(student_heights[n])
print(student_heights)
#for i in range(0,len(student_heights)):
totalhigh = sum(student_heights)
num_students=len(student_heights)
averagehigh=totalhigh/num_students
print(totalhigh)

