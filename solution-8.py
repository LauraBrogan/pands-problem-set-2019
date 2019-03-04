# Solution to Problem 8
# Program outputs today's date and time in the format "Monday, January 10th 2019 at 1:15pm"

# To start we import the Python datetime module.
import datetime

now = datetime.datetime.now()

print("Todays Date and time:")
%I = 
%d = 
print(now.strftime("%A, %B %d %Y at %I:%M %p"))



#Reference:https://www.saltycrane.com/blog/2008/06/how-to-get-current-date-and-time-in/
# Used lecture from week 6 as a base for the problem also looked at the Python tutorial.
# Laura Brogan 