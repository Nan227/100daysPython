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
# No max() and min() use
maxHeight = 0
for height in students_height:
  if height > maxHeight:
     maxHeight=height
print(f" The higtest of students height is {maxHeight}")

# No max() and min() use
minHeight = students_height[0]
for height in students_height:
  if height < minHeight:
     minHeight=height
print(f" The lowest of students height is {minHeight}")
