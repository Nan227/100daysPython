students_height=input("Enter students height 'cm': ").split()
for n in range(0, len(students_height)):
  students_height[n] =int(students_height[n])
print(students_height)

 #totalHeight =sum(student_height)
totalHeight=0
for height in students_height:
  totalHeight +=height
 
print(totalHeight)

# numberDtufent=len(student_height)
totalStudent = 0
for m in students_height:
  totalStudent += 1
print(totalStudent)


averageHeight = totalHeight/totalStudent
averageHeight = round(averageHeight, 0)
averageHeight = int(averageHeight) # without decimal
print(f" The average height of {totalStudent} students is {averageHeight} cm" )