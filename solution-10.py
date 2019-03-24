# Solution to Problem 10
# Display plot of punction x, x^2, 2^x in the range [0,4].
# Start by importing matplotlib.pyplot which  is a collection of command style functions that make matplotlib work like MATLAB. 
# Each pyplot function makes some change to a figure: e.g., creates a figure, creates a plotting area in a figure, plots some lines in a plotting area, decorates the plot with labels, etc
# I import matplotlib.pyplot as pl for short.
import matplotlib.pyplot as pl
# For this example x is two
x = 2
# Lines is the plot of each of the expressions in red. 
lines = pl.plot(x, x^2, 2^x,'r')
# Plotting for the range 0-4.
pl.plot([0,4])
# The graph has title name Plot of Functions 2019.
pl.title('Plot of Functions 2019')#
# The graphs y and x axis are labeled accordingly. 
pl.ylabel('Y Axis Values')
pl.xlabel('Axis Values')
# Diagram is displayed to the user. 
pl.show()


# Reference:https://matplotlib.org/1.4.2/users/pyplot_tutorial.html
# Reference: https://www.oreilly.com/library/view/python-data-science/9781491912126/ch01.html#help-and-documentation-in-ipython
# Laura Brogan 24/03/19