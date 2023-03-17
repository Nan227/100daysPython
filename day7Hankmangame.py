import random
#step1 choose the random word
list_word=["kanda","nareda","benjamin","anmieme","akane"]
answer_word = random.choice(list_word)
#print(answer_word)
#step2 asking user
guess=input("Guess letter: ").lower()
print(guess)