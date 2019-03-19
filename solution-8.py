# Solution to Problem 8
# Program outputs today's date and time in the format "Monday, January 10th 2019 at 1:15pm"

from datetime import datetime as dt

def suffix(d):
    return 'th' if 11<=d<=13 else {1:'st',2:'nd',3:'rd'}.get(d%10, 'th')

def custom_strftime(format, t):
    return t.strftime(format).replace('{S}', str(t.day) + suffix(t.day))

print(custom_strftime('%B {S}, %Y', dt.now())









# To start we import the Python datetime module.


#from datetime import datetime as dt
#now = dt.now()
#def suffix(d):
    # return 'th' if 11<=d<=13 else {1:'st',2:'nd',3:'rd'}.get(d%10, 'th')

#def custom_strftime(format, t):
   # return t.strftime(format).replace('{S}', str(t.day) + suffix(t.day))
#print("Todays Date and time:")
#print custom_strftime ('%B %d, %Y', dt.now())
#print (custom_strftime("%A, %B {S} %Y atdt.now() %I:%M %p"))

#print(now.strftime("%A, %B %d %Y at %I:%M %p"))


# Reference:https://www.saltycrane.com/blog/2008/06/how-to-get-current-date-and-time-in/
# Used lecture from week 6 as a base for the problem also looked at the Python tutorial.