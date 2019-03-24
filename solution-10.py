# Solution to Problem 10
# Display plot of punction x, x^2, 2^x in the range [0,4].
# Start by importing matplotlib.pyplot which  is a collection of command style functions that make matplotlib work like MATLAB. 
# Each pyplot function makes some change to a figure: e.g., creates a figure, creates a plotting area in a figure, plots some lines in a plotting area, decorates the plot with labels, etc
# I import it as pl for short.
import matplotlib.pyplot as pl
# For this example x is two
x = 2
lines = pl.plot(x, x^2, 2^x)
pl.plot([0,4])
pl.setp(color='grey', linestyle='-', linewidth=0.25, alpha=0.5) 
#pl.setp(lines 'color', 'y' 'linewidth', 10.0)
pl.ylabel('Plot of functions')
pl.show()


# use keyword args

# or MATLAB style string value pairs
#plt.setp(lines, 'color', 'r', 'linewidth', 2.0)
#https://matplotlib.org/1.4.2/users/pyplot_tutorial.html
#https://www.oreilly.com/library/view/python-data-science/9781491912126/ch01.html#help-and-documentation-in-ipython