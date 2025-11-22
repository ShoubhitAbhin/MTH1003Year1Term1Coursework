# group all imports at the top of the file
from math import floor
from scipy.special import jv
import numpy as np
import matplotlib as plt


# DO NOT EDIT THIS FUNCTION
def myfunction(x, test=False):

    if test:
        # for testing purposes only 
        w1 = rand() * 2 - 1
        w2 = rand() * 2 - 1
    else:
        # gain the last pairs of digits from the student number, to
        # obtain weights
        a  = myID()
        w1 = (a % 100) * 0.02 - 1.0
        w2 = (floor(a/100) % 100) * 0.02 - 1.0

    # some suitable functions to add together 
    y0 = jv(0, x)
    y1 = jv(1, x*2) * 0.75
    y2 = jv(2, x*4) * 0.5

    # to give the 'myfunction' weighted by the student number final digits 
    y = y0 + w1 * y1 + w2 * y2

    return y


# TASK 1: Write your myID function


# TASK 2: Write your code to produce a line plot using myfunction to
# generate the y values


# TASK 3: Write your numdiff function


# TASK 4: Test your numdiff function on a function of your choice


# TASK 5: Plotting f'(x) and f''(x) for the function f(x) given by myfunction


# TASK 6: Write your findroot function


# TASK 7: Test your findroot function on a function of your choice


# TASK 8: Apply your findroot function to f(x) defined by myfunction
