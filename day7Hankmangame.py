import random
#step1 choose the random word
list_word=["kanda","nareda","benjamin","anmieme","akane"]
answer_word = random.choice(list_word)
#print(answer_word

number_line = len(answer_word)
print(number_line)
for i in range(0,number_line+1):
  line ="_" *i
print("The word is "+line)

#step2 asking user
guess=input("Guess letter: ").lower()
#print(guess)
#while guess != answer_word:
  #print(guess)
for j in answer_word:
  if guess == j:
    result = True
  else:
    result = False
print(result)

if (result == True):
  line = guess
  print(line)
