# Solution to Problem 2
# Is today a day that begins with the letter T 

# To start we import the Python datetime module.
import datetime


# If today is Tuesday or Thursday please display to the user that yes today begins with a T.
if datetime.datetime.today().weekday() == 1:
    print("Yes today begins with a T.")

elif datetime.datetime.today().weekday() == 3:
    print("Yes today begins with a T.")
        
# If today is not Tuesday or Thursday please display to the user that unfortunately today is not a day that begins with a T.
else:
    print("Unfortunately today is not a day that begins with T.")

# Used lecture on Tuesday program as a base for the problem.

# Laura Brogan 19/02/2019