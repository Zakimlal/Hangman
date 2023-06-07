import random

import hangman_words
word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

import hangman_art
print(hangman_art.logo)

#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    print(f'Your word in contained {word_length} letters')
    print(f'You still have {lives} chances')
    guess = input("Guess a letter: ").lower()

    import os
    os.system('cls||clear')

    if guess in display:
        print(f'You\'ve already guessed {guess}')

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            print("Nice You discovered a letter!")

    #Check if user is wrong.
    if guess not in chosen_word:
        lives -= 1
        print(f'You guessed {guess}, that\'s not in the word. You lose a life')
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f'The word was : {chosen_word}')

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(hangman_art.stages[lives])