# Solution to Problem 8
# Program outputs today's date and time in the format "Monday, January 10th 2019 at 1:15pm"

# To start we import the Python datetime module.
import datetime

now = datetime.datetime.now()

print("Todays Date and time:")
print(now.strftime("%A,%B,%d,%h,%M,%I,%p"))
# Used lecture from week 6 as a base for the problem also looked at the Python tutorial.

# Laura Brogan 19/02/2019