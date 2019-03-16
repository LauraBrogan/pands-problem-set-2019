# Solution to Problem 8
# Program outputs today's date and time in the format "Monday, January 10th 2019 at 1:15pm"

# To start we import the Python datetime module.
import datetime 

now = datetime.datetime.now()
day = today.day
#date_string = today.strftime('%A, %B %# %Y at %I:%M %p')


print("Todays Date and time:")
if (3 < day < 21) or (23 < day < 31):
  day = str(day) + 'th'
else:
  suffixes = {1: 'st', 2: 'nd', 3: 'rd'}
  day = str(day) + suffixes[day % 10]

#print(date_string.replace('#', day), end='')
print(now.strftime("%A, %B %d# %Y at %I:%M %p"))


# Reference Verbatim https://www.robjwells.com/2013/10/date-suffixes-in-python/
# Reference:https://www.saltycrane.com/blog/2008/06/how-to-get-current-date-and-time-in/
# Used lecture from week 6 as a base for the problem also looked at the Python tutorial.
# Laura Brogan 