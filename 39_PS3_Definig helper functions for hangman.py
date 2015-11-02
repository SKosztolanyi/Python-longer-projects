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
    



def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    
    # This simple function returns false if all the letters from secret word are not in lettersGuessed
    
    for s in str(secretWord):
        if s not in list (lettersGuessed):
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
    guess = ''
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