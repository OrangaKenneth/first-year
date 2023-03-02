# Problem Set 2, hangman.py
# Name:Kenneth Oranga
# Collaborators:Office Hours/Christine Lee
# Time spent: 1 hr 21 mins

import random
import string

# -----------------------------------
# HELPER CODE
# -----------------------------------

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    returns: list, a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(" ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

# -----------------------------------
# END OF HELPER CODE
# -----------------------------------


# Load the list of words to be accessed from anywhere in the program
wordlist = load_words()

def has_player_won(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: boolean, True if all the letters of secret_word are in letters_guessed,
        False otherwise
    """
    checker = 0
    for char in secret_word:
      if char in letters_guessed:
        checker += 1
    return(checker == len(secret_word))



def get_word_progress(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters and asterisks (*) that represents
        which letters in secret_word have not been guessed so far
    """
    word_p = ''
    for l in  secret_word:
      if l in letters_guessed:
        word_p += l
      else:
        word_p += '*'
    return word_p

def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    """
    available_letter = ''
    for l in string.ascii_lowercase:
      if l not in letters_guessed:
        available_letter+=l #adds all letters not guessed
    return available_letter# output string

def with_help_f(secret_word,rest):
    """
    secret_word : string, to be guessed
    get_available_letters: string,give all the possible letters that have not been guessed yet

    return: should return a random letter that is in both the secret word and the available_letter string
    """
    choose_from = ''
    for l in set(secret_word):
      if l in rest:
        choose_from += l
    new = random.randint(0, len(choose_from)-1)
    revealed_letter = choose_from[new]
    return(revealed_letter)
    
def hangman(secret_word, with_help):
    """
    secret_word: string, the secret word to guess.
    with_help: boolean, this enables help functionality if true.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses they start with.

    * The user should start with 10 guesses.

    * Before each round, you should display to the user how many guesses
      they have left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a single letter (or help character '$'
      for with_help functionality)

    * If the user inputs an incorrect consonant, then the user loses ONE guess,
      while if the user inputs an incorrect vowel (a, e, i, o, u),
      then the user loses TWO guesses.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    -----------------------------------
    with_help functionality
    -----------------------------------
    * If the guess is the symbol $, you should reveal to the user one of the
      letters missing from the word at the cost of 3 guesses. If the user does
      not have 3 guesses remaining, print a warning message. Otherwise, add
      this letter to their guessed word and continue playing normally.

    Follows the other limitations detailed in the problem write-up.
    """
    print('Welcome to Hangman')
    print(f'I am thinking of a word that is {len(secret_word)} letters long')
    guess_n0 = 10
    letters_guessed = []

    while guess_n0 > 0:
      
      if has_player_won(secret_word, letters_guessed):
        print('-----------')
        print('Congratulations, you won!')
        total = ((guess_n0+2 * len(set(secret_word)))+(3*len(secret_word)))
        print(f'Your total score for this game is: {total}')
        break
      
      else:
        print('----------')
        print(f'You have {guess_n0} guesses left')
        print(get_available_letters(letters_guessed))
        guessed_letter = str.lower(input('Please guess a letter: '))

        if guessed_letter in letters_guessed:
            print("Oops! You've already guessed that letter:",get_word_progress(secret_word, letters_guessed))
        else:
          if str.isalpha(guessed_letter):
            if (guessed_letter in secret_word) and (guessed_letter not in letters_guessed):
              letters_guessed.append(guessed_letter)
              print('Good guess:',get_word_progress(secret_word, letters_guessed))
            if guessed_letter not in secret_word:
              vowels = ['a','e','i','o','u']
              if guessed_letter in vowels:
                guess_n0 -= 2
              else:
                guess_n0 -= 1
              print("Oops! That letter is not in my word:", get_word_progress(secret_word, letters_guessed))
              letters_guessed.append(guessed_letter)
          
          else:
            if (guessed_letter == '$') and with_help == True:
              if (guess_n0 < 3):
                print('Oops! Not enough guesses left:', get_word_progress(secret_word, letters_guessed))
              else:
                l_reveal = with_help_f(secret_word,get_available_letters(letters_guessed))
                print(f'Letter revealed:', l_reveal) 
                letters_guessed.append(l_reveal)
                print('Good guess:', get_word_progress(secret_word, letters_guessed))
                guess_n0 -= 3
            else:
              print('Oops! That is not a valid letter. Please input a letter from the alphabet:', get_word_progress(secret_word, letters_guessed))

    if guess_n0 <= 0:
      print('---------')
      print('Sorry you ran out of guesses. The word was', secret_word)
      



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the lines to test

if __name__ == "__main__":
    # To test your game, uncomment the following three lines.

    secret_word = choose_word(wordlist)
    with_help = True
    hangman(secret_word, with_help)

    # After you complete with_help functionality, change with_help to True
    # and try entering "$" as a guess!

    ###############

    # SUBMISSION INSTRUCTIONS
    # -----------------------
    # It doesn't matter if the lines above are commented in or not
    # when you submit your pset. However, please run test_ps2_student.py
    # one more time before submitting to make sure all the tests pass.
    pass
