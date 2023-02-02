print("\nWelcome to the Rock and scissor game")
youChoice=str(input("Enter Rock, Peper, or Scissor: R,P,S: "))
choice=["R","P","S"]

computerChoice = random.randint(0,3)
print(f"Computer choose {computerChoice} ")
if computerChoice ==0:
  computerChoice = "R"
  
elif computerChoice ==1:
  computerChoice = "P"
else:
  computerChoice = "S"
# check the computer choice
print(f"Computer chooses {computerChoice} and your chooses {youChoice} \nthe reasult is ")
# compair your choice and computure choice it who is win
if youChoice==computerChoice:
  print("You are tie")
  #youChoice[R] and computerChoice[S]
elif youChoice=="R" and computerChoice=="S":
  print("You win")
  #youChoice[P] and computerChoice[R]
elif youChoice=="P" and computerChoice=="R":
  print("You win")
  #youChoice[S] and computerChoice[P]
elif youChoice=="S" and computerChoice=="P":
  print("You win")
else:
  print("You lose")
  
