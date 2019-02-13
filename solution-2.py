# Solution to Problem 2
# Is today a day that begins with the letter T 

import datetime


if datetime.datetime.today().weekday() == 1:
    print("Yes today begins with a T.")
    
if datetime.datetime.today().weekday() == 3:
    print("Yes today begins with a T.")

# If today is Tuesday  or a Thursday please display to the user that yes today begins with a T. 
 
else:
    print("Unfortunately today is not a day that begins with T.")

# If today is not Tuesday or Thursday please display to the user that unfortunately today is not a day that begins with a T.

# Laura Brogan 10/02/2019