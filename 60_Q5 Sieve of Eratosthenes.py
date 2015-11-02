def primesList(N): # AKA Sieve of Eratosthenes
# It is a mathematical function, that finds all the prime numbers up to a certain number.
    '''
    N: an integer
    Returns a list of prime numbers
    ''' 
    if N==2: # This is the simplest case, because 2 is first and smallest prime number that will always be in the list of all the prime numbers up to certain point.
        return [2]
    elif N<2:
        return [] # I simply create an empty list to which I will be adding integers on the way.
    r=range(3,N+1,2) # I set this range to put only every second number and to start with 3 as the first prime number after 2.
    root = N ** 0.5
    half=(N+1)/2-1
    i=0
    m=3
    while m <= root:
	if r[i]:
		j=(m*m-3)/2
		r[j]=0
		while j<half:
			r[j]=0
			j+=m
# This was mathematical expression of getting the correct numbers only, eg. prime numbers
	i+=1
	m=2*i+3
    return [2]+[x for x in r if x] # I substitute a number in the list with the same number, adding one number to the end of list.
