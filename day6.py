
def  turn_left(): 
  move()
  move()
 
  
def  jump():
  move()
  turn_left()
  move()
  turn_left()
  move()
  turn_left()
 
while not at_goal:
  jump()
