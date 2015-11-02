def getSublists(L, n):
    '''
    This function returns a list of all possible sublists in L of length n 
    without skipping elements in L.
    The sublists in the returned list should be ordered in the way they appear in L, 
    with those sublists starting from a smaller index being at the front of the list.
    '''
    subs = []
    temp = []
    for i in range(len(L)-n+1):
        temp = L[i:i+n]
        subs.append(temp)
    return subs
        
test = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2]
test2 = [1, 1, 0, 1, 1, 4]
print getSublists(test, 4)
print getSublists(test2, 2) 

def longestRun(L):
    temp = []
    for i in range(len(L)-1):
        if L[i] > L[i+1]:
            pass
        while L[i] <= L[i+1]:    
        #if L[i] <= L[i+1]:
            k = L[i]
            temp.append(k)
            print temp
            i += 1
    print temp
    return len(temp)
    
print longestRun(test)

def howlong(L):
    counter = 1
    longest = 1
    for i in range(len(L)-1):
        if L[i] <= L[i+1]:
            counter += 1
            if counter > longest:
                longest = counter
        if L[i] > L[i+1]:
            counter = 1
    return longest
    
print howlong(test2)
             
