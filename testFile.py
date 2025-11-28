from math import floor
from scipy.special import jv
import numpy as np
import matplotlib.pyplot as plt

# DO NOT EDIT THIS FUNCTION
def myfunctionNNNN(x, test=False):

    if test:
        # for testing purposes only 
        w1 = rand() * 2 - 1
        w2 = rand() * 2 - 1
    else:
        # gain the last pairs of digits from the student number, to
        # obtain weights
        a  = myIDDDDD()
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
"""
This function returns my candidate number as a integer - myId: void -> int
"""
def myIDDDDD(): 
    return 468673

xVals = [1,2,3,4,5]
yVals = []
for n in range(5):
    yVals.append(myfunctionNNNN(xVals[n]))
    
for a in range(5):
    print(yVals[a])

print("this is my function for x=5")
print(myfunctionNNNN(5))