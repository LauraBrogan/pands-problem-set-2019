# Solution to Problem 2
# Is today a day that begins with the letter T 

import datetime

if datetime.datetime.today().weekday() == 1:
  print("Yes today begins with a T.")
  if datetime.datetime.today().weekday() == 3:
    print("Yes today begins with a T.")
else:
    print("Unfortunately today is not a day that begins with T.")