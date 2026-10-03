import random

words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()

HANGMANPICS = ['''
  +---+

  |   |
      |
      |
      |
      |
=========''', '''
  +---+

  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+

  |   |
  O   |

  |   |
      |
      |
=========''', '''
  +---+

  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+

  |   |
  O   |
 /|\\  |
      |
      |
=========''', '''
  +---+

  |   |
  O   |
 /|\\  |
 /    |
      |
=========''', '''
  +---+

  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========''']

word_to_guess = random.choice(words)
_word = ["_"] * len(word_to_guess)
print(f"Welcome to Hamgman game (:\n")
print(" ".join(_word))
tries = 6
guessd_letters = []
print(HANGMANPICS[0])

while "_" in _word and tries > 0:
    letter_guess = input("Please guess a letter: ").lower().strip()
    
    if letter_guess in guessd_letters:
        print("you already guessd that, try again!")
        print(f"You have {tries} more tries")
        continue
        
    guessd_letters.append(letter_guess)
    
    if letter_guess not in word_to_guess:
        tries -= 1
        print(HANGMANPICS[6 - tries])
    else:
        for position in range(len(word_to_guess)):
            if word_to_guess[position] == letter_guess:
                _word[position] = letter_guess
                
    print(" ".join(_word))
    print(f"You have {tries} more tries")

if tries == 0:
    print(HANGMANPICS[6])
    print("you have no more tries!, play again!")
else:
    print("\n" + " ".join(_word))
    print("(*:*******(:")
