import random
# step 1  random word
word_list = ["wordlist", "football", "watermelon", "smile","lucky"]
chosen_word = random.choice(word_list)

#step2
guess = input ("Guess a letter: ").lower()

#step3 check if the letter == chosen_word
for letter in chosen_word:
  if letter == guess:
    print ("Right")
  else:
    print("Wrong")