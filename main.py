import random
from hangman_art import stages, logo
from hangman_words import word_list
from replit import clear
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(f"{logo}\n")
print("\n")
#Create blanks
display = []
for _ in range(word_length):
    display += "_"
  
#Print blanks
print(f"The unknown word contains {word_length} letters: {' '.join(display)}\n")

#Create empty list to hold previous wrong guesses[]
wrong_guesses = []

while not end_of_game:
  
  guess = input("Guess a letter: ").lower()
  
  clear()
  
  if guess in display:
    print(f"You've already guessed {guess}")
  else:
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        wrong_guesses += guess
        print(f"You guessed {guess}, that's not in the world. You lose a life.\n")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.\n")
            print(f"The word was: {chosen_word}\n")

    #Join all the elements in the list and turn it into a String.
    if lives > 0:
      print(f"So far you've guessed incorrectly: {', '.join(wrong_guesses)}\n")
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

  print(stages[lives])