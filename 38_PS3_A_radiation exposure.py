# This part is provided by the grader
# I only define the radiationExposure, with using predefined function f

# This part is copied from the grader to have an idea of the function it will use

Cobalt-60.Half-life: 5.27 years. Initial Activity: 10 MBq.
Find total exposure from years 5 - 11.

def f(x):
    '''
The technique of finding the area under a curve is called integration.
This comes to us from calculus.
What we're doing in this problem is an approximation of finding the integral
under the curve using the summation of rectangular areas known as a Riemann integral.
	'''
	import math
	return 10*math.e**(math.log(0.5)/5.27 * x)
	
def radiationExposure(start, stop, step):
    '''
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the 
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.
 
    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
      the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to 
      between start and stop times.
    '''
    # FILL IN YOUR CODE HERE...    
    total = 0
    current = start
    while current < stop:
        total += f(current) * step
        current += step
    return total