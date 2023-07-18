import random

print("\nWelcome to the Rock and scissor game")
youChoice=int(input("Enter '0' for Rock, '1' for Peper, or '2' for Scissor:  "))
#rock
rock ='''Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

 '''
#paper
paper='''Paper
    _______
---'   ____)______
      (____________)
      (_______________)
      (____________)
---.__(________)

 ''' 
# Scissors
scissor='''Scissor
    _______
---'   ____)________
       _____________)
       ________________)
      (____)
---.__(___)
'''
computerChoice = random.randint(0,2)

# check the computer choice

print(f"Computer chooses {computerChoice} ")
# compair your choice and computure choice it who is win
if computerChoice==0:
  print(rock)
elif computerChoice==1:
  print(paper)
else:
  print(scissor) 
print(f"and your chooses {youChoice}  ")
# compair your choice and computure choice it who is win
if youChoice==0:
  print(rock)
elif youChoice==1:
  print(paper)
else:
  print(scissor)
print(f"the reasult is ")
#check 
if youChoice==computerChoice:
  print("You are tie")

  #youChoice[R] and computerChoice[S]
elif youChoice== 0 and computerChoice==2:
  print("You win")
  #youChoice[P] and computerChoice[R]
elif youChoice==2 and computerChoice==1:
  print("You win")
  #youChoice[S] and computerChoice[P]
elif youChoice==2 and computerChoice==1:
  print("You win")
else:
  print("You lose")
  