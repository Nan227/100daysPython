import random
# step 1  random word
word_list = ["wordlist", "football", "watermelon", "smile","lucky"]
chosen_word = random.choice(word_list)
wordlength = range(len(chosen_word))
#step2
guess = input ("Guess a letter: ").lower()
print(f' the solution word is {chosen_word}')
#step3 check if the letter == chosen_word
display = []
for _ in wordlength:
  display += "_"
print(display)

for position in wordlength:
  letter =chosen_word[position]
  if letter == guess:
    display[position] = letter
 