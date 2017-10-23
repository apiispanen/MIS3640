# Hangman game
#

# -----------------------------------

import random

WORDLIST_FILENAME = "words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

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
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    correct_letters = []
    for letter in secretWord:
        if letter in lettersGuessed:
            correct_letters.append(letter)

    word_progress = ''.join(correct_letters)
    if word_progress == secretWord:
        return True
    else:
        return False 



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    words_correct = []
    secret_list = list(secretWord)
    for letter in secretWord:
        if letter in lettersGuessed:
            words_correct.append(letter)
        else:
            words_correct.append('_ ') 
    words_correct = ''.join(words_correct)
    return words_correct


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # Hint: You might consider using string.ascii_lowercase, which
    # is a string comprised of all lowercase letters.
    alph = 'abcdefghijklmnopqrstuvwxyz'
    # FILL IN YOUR CODE HERE...
    for letter in lettersGuessed:
        if letter in alph:
           alph = alph.replace(letter,'')
    return alph


def hangman(secretWord):
    loadWords()
    lives = 8
    letters_guessed = []
    secretWord = secretWord.lower()
    
    print('')
    print('Welcome to Hangman! Let \'s play!')
    #secretWord = chooseWord(WORDLIST_FILENAME).lower()
    print('I am thinking of a word that is', len(secretWord), 'letters long!')
    print ("_ " * len(secretWord))
    while lives >= 0:
        print('You have', lives, 'lives left')
        print('Available letters: ', getAvailableLetters(letters_guessed))
        guess = input('Please guess a letter: ').lower()
        print('----------------------------------------------------')
        while len(guess)>1 or guess not in getAvailableLetters(letters_guessed):
            guess = input('Invalid, please choose again: ').lower() 
        letters_guessed.append(guess)
        print(getGuessedWord(secretWord, letters_guessed))
        
        if isWordGuessed(secretWord,letters_guessed):
            print('Congrats, you\'ve won!! The word was', secretWord)
            break
        if guess in secretWord:
            print('Good guess!!')
        else:
            print('Nice try. That\'s not in the word!')
            lives -=1
    if not isWordGuessed(secretWord,letters_guessed):
        print('You ran out of lives. The word was', secretWord,'. You lose!')
   
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
