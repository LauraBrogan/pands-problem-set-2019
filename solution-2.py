# Solution to Problem 2
# Is today a day that begins with the letter T 

import datetime

if datetime.datetime.today().weekday() == 1:
    print("Yes today begins with a T.")
if datetime.datetime.today().weekday() == 3:
    print("Yes today begins with a T.")

# If today is Tuesday please display to the user that yes today begins with a T. 
 
# If today is Thursday please display to the user that yes today begins with a T.

while datetime.datetime.today().weekday() == 0:
    while datetime.datetime.today().weekday() == 2:
        while datetime.datetime.today().weekday() == 5:
            while datetime.datetime.today().weekday() == 6:
                while datetime.datetime.today().weekday() == 7:
                     print("Unfortunately today is not a day that begins with T.")
# If today is not Tuesday or Thursday please display to the user that unfortunately today is not a day that begins with a T.

# Laura Brogan 10/02/2019