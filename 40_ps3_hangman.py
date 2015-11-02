# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
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
    
    # This simple function returns false if all the letters from secret word are not in lettersGuessed
    
    for s in secretWord:
        if s not in lettersGuessed:
            return False
    return True
    
    # To test this function, I need to put the answer in the following form:
    # isWordGuessed('apple', ['a', 'e', 'i', 'k', 'p', 'r', 's'])



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    guess = ""
# I indicate that guess is a string. I create an empty string before the function and then fill in the letters and blanks when adding letters.
    for s in secretWord:
# with this line in function I give to every letter in secretWord one "s"
# the count of s indicates the lenght of the secretWord
        if s in lettersGuessed:
            guess += s
        else:
            guess += "_ "
    return guess
    
    # this is example output:
    # Function call: getGuessedWord('coconut', ['r', 'j', 'l', 'h', 'a', 'u', 'k', 'o', 'x', 'w'])
    # output: '_ o_ o_ u_ '


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    available = string.ascii_lowercase
    for s in available: 
        if s in lettersGuessed:
            available = available.replace(s, "")
    # Strings are immutable, therefore I can't use operator like -=
    # I need to replace the old string with new one, without the letters mentioned
    return available
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print "Welcome to the game Hangman!"
    print "I am thinking of a word that is ",+(len(secretWord)), " letters long."
    print "___________________"
    lettersGuessed = []
    badGuess = 0
    letters = string.ascii_lowercase
 
    while badGuess < 8 and not isWordGuessed(secretWord, lettersGuessed):
        print "You have", 8 - badGuess, "guesses left."
        print "Available letters:", letters
        guess = raw_input("Please guess a letter: ").lower()
 
        if guess in lettersGuessed:
            print("Oops! You've already guessed that letter: " +
                getGuessedWord(secretWord, lettersGuessed))
        elif guess in secretWord:
            lettersGuessed.append(guess)
            print "Good guess:", getGuessedWord(secretWord, lettersGuessed)
        else:
            badGuess += 1
            lettersGuessed.append(guess)
            print("Oops! That letter is not in my word: " + 
                getGuessedWord(secretWord, lettersGuessed))
 
        letters = getAvailableLetters(lettersGuessed)
 
        print "_____________________"
 
    if isWordGuessed(secretWord, lettersGuessed):
        print "Congratulations, you won!"
    else:
        print("Sorry, you ran out of guesses. The word was " + secretWord + 
             ".")
 
# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)
 
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
