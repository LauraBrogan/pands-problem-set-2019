# Solution to Problem 8
# Program outputs today's date and time in the format "Monday, January 10th 2019 at 1:15pm"
# To start we import the Python datetime module.


from datetime import datetime as dt
import time
now = dt.now()
#def suffix(d):
    # return 'th' if 11<=d<=13 else {1:'st',2:'nd',3:'rd'}.get(d%10, 'th')
t = time.localtime()
suffix = 'st' if t.tm_mday in [1,21,31] else 'nd' if t.tm_mday in [2, 22] else 'rd' if t.tm_mday in [3, 23] else 'th'


#def custom_strftime(format, t):
   # return t.strftime(format).replace('{S}', str(t.day) + suffix(t.day))
print("Todays Date and time:")
print(time.strftime('%d%%s %B %Y', t) % suffix)
#print custom_strftime ('%B %d, %Y', dt.now())
#print (custom_strftime("%A, %B {S} %Y atdt.now() %I:%M %p"))

#print(time.strftime("%A, %B %d %Y at %I:%M %p"))


# Reference:https://www.saltycrane.com/blog/2008/06/how-to-get-current-date-and-time-in/
# Used lecture from week 6 as a base for the problem also looked at the Python tutorial.