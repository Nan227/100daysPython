print("X O game")
row1 = [ " ", " ", " "]
row2 = [ " ", " ", " "]
row3 = [ " ", " ", " "]
map = [row1, row2, row3]

print(f"{row1} \n{row2} \n{row3}")
position = input (" Where do you want to input 'x'? :")
#write the code
#horizonal = int(position[0])
#vertical = int(position[1])
#serect_row= map[vertical-1]
#serect_row[horizonal-1] = "X"
y= int(position[0])
x= int(position[1])
map[x-1][y-1]="o"
print(f"{row1} \n{row2} \n{row3}")
