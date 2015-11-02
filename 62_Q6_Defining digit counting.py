#Write a recursive Python function, given a non-negative integer N, to count and return the number of occurrences of the digit 7 in N.
#This function has to be recursive; you may not use loops! This function takes in one integer and returns one integer.

# I want to create a recursive function that counts number of occurence of a digit in a number:
def count7(N):
    '''
    N: a non-negative integer
    '''
    # Your code here
    N=str(N) # At first I change the number of type int to a string, because I can compare slice a word based on it's characters positions.
    times = 0 # I set the starting count to 0 times.
 #   if len(N)>= 1: # condition for countin
    if N == "":
        return times
    elif N == "7": #position of digit
        return times+=1
    else:    
        return count7(N[:-1]) # this is the recursive call to the same string without the last letter
    return times  