# group all imports at the top of the file
from math import floor
from scipy.special import jv
import numpy as np
import matplotlib.pyplot as plt


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

"""
This function returns my candidate number as a integer - myId: void -> int
"""
def myID(): 
    return 468673


# TASK 2: Write your code to produce a line plot using myfunction to
# generate the y values

"""
The following code creates the x and y value arrays.
"""
x = np.arange(0,10.1,0.01) # from 0-10 inclusive in steps of 0.1
y = myfunction(x)

"""
The following code creates a graph with linewidth lw and adds the x-axis, y-axis and title specified. The file is saved and the show file command has been commented out.
"""
lw = 2
plt.clf() # clears the plot (source: https://www.activestate.com/resources/quick-reads/how-to-clear-a-plot-in-python/)
plt.plot(x,y,linewidth=lw)
plt.xlabel("x")
plt.ylabel("myfunction(x)")
plt.title("A Plot of myFunction")
plt.savefig("yplot.png")
 # plt.show()


# TASK 3: Write your numdiff function

"""
The following code is for my numerical differentation function.
"""
def numdiff(h, y):
    # The parameter h is the spacing (i.e. xn+1 - xn)
    # The parameter y is a numpy array of length k with k y-values specified
    # numdiff: int, list -> list, list

    numElements = len(y) # the number of elements in the PYTHON list
    dy = [] # creates an empty PYTHON list, as appending to numpy arrays is inefficient (creates a new array everytime), for the first derivative approximations
    ddy = [] # creates another empty list, this time for the second derivative approximations
    
    """
    The following loop appends the interior values of dy and ddy to their respective lists.
    """
    for n in range(1,numElements-1,1):
        dy.append((y[n+1] - y[n-1])/(2*h))
        ddy.append((y[n+1]-(2*y[n])+y[n-1])/(h**2))

    """
    The following loop adds the end cases to the dy and ddy lists.
    """
    dyFirstValue = (-y[2]+(4*y[1])-(3*y[0]))/(2*h)
    ddyFirstValue = (-y[3]+(4*y[2])-(5*y[1])+(2*y[0]))/(h**2)
    dyLastValue = ((3*y[numElements-1])-(4*y[numElements-2])+y[numElements-3])/(2*h)
    ddyLastValue = ((2*y[numElements-1])-(5*y[numElements-2])+(4*y[numElements-3])-(y[numElements-4]))/(h**2)
    dy.insert(0,dyFirstValue)
    ddy.insert(0,ddyFirstValue)
    dy.append(dyLastValue)
    ddy.append(ddyLastValue)

    return dy, ddy # returns the lists dy and ddy

# TASK 4: Test your numdiff function on a function of your choice

"""
The following code creates a function h(x) which can be differentiated twice
"""

def g(x):
    # my function is cos(x)
    # g(x): reals -> [-1,1]
    return np.cos(x) 

hVal = 0.01 # the spacing between each consecutive x value, which is predetermined

xValues = np.arange(0,10.1,hVal) # an array of predetermined x-values
yValues = [] # an empty array which will be populated with the corresponding y-values

"""
The following loop populates the yValues array with the appropriate y values.
"""
for n in range(len(xValues)):
    yValues.append(g(xValues[n]))

 
dy, ddy = numdiff(hVal,yValues) # the return values of the numdiff function are stored in the variables dy and ddy respectively

"""
The following functions define the actual first and second derivatives for my function g(x)
"""

def dyActual(x):
    # dyActual: int -> int
    return ((np.sin(x)) * -1)

def ddyActual(x):
    # ddyActual: int -> int
    return ((np.cos(x)) * -1)

dyActualValues = [] # empty list which will be populated with the real values of dy (i.e. values of dy calculated using the known g'(x) for my function g(x) rather than numerically using the numdiff function)
ddyActualValues = [] # empty list which will be populated with the real values of dy (i.e. values of ddy calculated using the known g''(x) for my function g(x) rather than numerically using the numdiff function)


for a in range(len(xValues)): # this loop populates the dyActualValues and ddyActualValues list as described above
    dyActualValues.append(dyActual(xValues[a]))
    ddyActualValues.append(ddyActual(xValues[a]))


lw = 2 # define the linewidth
plt.clf() # clears the plot (source: https://www.activestate.com/resources/quick-reads/how-to-clear-a-plot-in-python/)
plt.plot(xValues,dy,linewidth=lw,label="dy") # plot the line for dy
plt.plot(xValues,ddy,linewidth=lw,label="ddy") # plot the line for ddy
plt.plot(xValues,dyActualValues,linewidth=lw,label="dyActual: g'(x)=-sin(x)",linestyle=":", color="k") # linestyle and colour to show the actual vs numdiff calculated lines when they overlap (source: https://www.geeksforgeeks.org/python/linestyles-in-matplotlib-python/)
plt.plot(xValues,ddyActualValues,linewidth=lw,label="ddyActual: g''(x)=-cos(x)",linestyle=":",color="b")
plt.xticks(np.arange(0, 11, step=1)) # add labels for every integer x between 0 and 10 (source: https://saturncloud.io/blog/how-to-set-xaxis-values-in-matplotlib-python-a-guide/#:~:text=To%20set%20the%20x%2Daxis,the%20labels%20for%20these%20ticks.&text=In%20this%20example%2C%20np.,with%20a%20step%20of%201.)
plt.legend() # add a legend
plt.xlabel("x")
plt.ylabel("dy|a & ddy|a for some x=a")
plt.title("A Plot of the First & Second Derivatives of g(x)=cos(x)")
# plt.show()
plt.savefig("dyddytest.png")


# TASK 5: Plotting f'(x) and f''(x) for the function f(x) given by myfunction
hValForMyFunctionPlot = 0.1
xValuesForMyFunction = np.arange(0,10.1,hValForMyFunctionPlot)
yValuesForMyFunction = []

for i in range(len(xValuesForMyFunction)):
    yValuesForMyFunction.append(myfunction(xValuesForMyFunction[i]))

dyForMyFunction, ddyForMyFunction = numdiff(hValForMyFunctionPlot, yValuesForMyFunction)

lw = 2
plt.clf() # clears the plot (source: https://www.activestate.com/resources/quick-reads/how-to-clear-a-plot-in-python/)
plt.plot(xValuesForMyFunction,dyForMyFunction,linewidth=lw,label="dyForMyFunction")
plt.plot(xValuesForMyFunction,ddyForMyFunction,linewidth=lw,label="ddyForMyFunction")
plt.legend()
plt.xlabel("x")
plt.ylabel("dy|a & ddy|a for some x=a")
plt.title("A Plot of the First & Second Derivatives of myFunction")
# plt.show()
plt.savefig("dyddyplot.png")


# TASK 6: Write your findroot function

def findroot(function,x1,x2): # findroot: function, int, int -> float, int
    y1 = function(x1) # calculates the y value associated with x0
    y2 = function(x2) # calculates the y value associated with x1

    counter = 2 # initialises a counting variable which will count the number of iterations
    magnitude = False # initialise a magnitude variable which is set to false, indicating that the magnitude criteria has not been met yet
    hasConverged = False # a boolean which will determine the output sent to the user

    while (counter <=20 and magnitude == False):
        nextX = ((x1 * function(x2)) - (x2 * function(x1)))/(function(x2) - function(x1))

        x1 = x2 # the current value of x2 is now stored in x1
        x2 = nextX # the next value of x is now stored in x2
        nextX = 0
        counter = counter + 1 # adds one to the counter

        value = abs(function(x2))
        if value <= 10e-6:
            magnitude = True

    if magnitude == True:
        hasConverged = True

    if hasConverged == True:
        print(f'The function has converged to the root {x2}')
        return x2
    else:
        print("The calculation has not converged")
        return 0


# TASK 7: Test your findroot function on a function of your choice 

"""
Define a function h(x) which has at least one root
"""

def h(x):
    # let h(x) = x^2 - 4x + 3 = (x-3)(x-1), meaning it has roots at x=1,3
    return ((x**2) - (4*x) + 3)

findroot(h,0.9,1.1)
"""
The output is: "The function has converged to the root 1.0000006611963688"
"""



# TASK 8: Apply your findroot function to f(x) defined by myfunction

findroot(myfunction,1,3)
"""
The output is: "The function has converged to the root 2.370640317019967". This seems correct as we can see from the yplot.png file that the function seems to have a value of 0 around the point x=2.3, which is close to the root we have found
"""