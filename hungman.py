def play_word_guessing_game(answer_word):
    guessed_word = ['_'] * len(answer_word)
    attempts_left = 6  # set a limit on the number of incorrect attempts

    while attempts_left > 0 and '_' in guessed_word:
        print(" ".join(guessed_word))  # print the current state of the guessed word
        guess = input("Guess a letter: ").lower()

        if guess in answer_word:
            for i in range(len(answer_word)):
                if answer_word[i] == guess:
                    guessed_word[i] = guess
            print("Correct!")
        else:
            attempts_left -= 1
            print("Incorrect! You have {} attempts left.".format(attempts_left))

    if attempts_left == 0:
        print("Sorry, you lost! The answer was {}.".format(answer_word))
    else:
        print("Congratulations, you won! The answer was {}.".format(answer_word))
print(play_word_guessing_game("word"))