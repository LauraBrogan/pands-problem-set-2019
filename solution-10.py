# Solution to Problem 10

import matplotlib.pyplot as pl
x = 2
lines = pl.plot(x, x^2, 2^x)
pl.plot([0,4])
pl.setp(lines, color='b', linewidth=4.0)
pl.show()

pl.ylabel('Plot of functions')




# use keyword args

# or MATLAB style string value pairs
#plt.setp(lines, 'color', 'r', 'linewidth', 2.0)
#https://matplotlib.org/1.4.2/users/pyplot_tutorial.html