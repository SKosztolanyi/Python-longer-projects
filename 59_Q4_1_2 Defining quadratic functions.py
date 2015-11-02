# -*- coding: utf-8 -*-
# Q 4_1
#Write a Python function, evalQuadratic(a, b, c, x), 
#that returns the value of the quadratic a⋅x2+b⋅x+c.

def evalQuadratic(a, b, c, x):
    '''
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    '''
    # Your code here
    return a*(x**2)+b*x+c
    
    
def twoQuadratics(a1, b1, c1, x1, a2, b2, c2, x2):
    '''
    a1, b1, c1: one set of coefficients of a quadratic equation
    a2, b2, c2: another set of coefficients of a quadratic equation
    x1, x2: values at which to evaluate the quadratics
    '''
    # Your code here
    function1 = evalQuadratic(a1, b1, c1, x1)
    function2 = evalQuadratic(a2, b2, c2, x2)
    sumtotal = function1 + function2
    return sumtotal