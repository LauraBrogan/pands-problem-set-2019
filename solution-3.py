# Solution to Problem 3
# Print all numbers between 1,000 and 10,000 that are divisible by 6 but not 12.

# Identify Lower and upper limits. Lower = 1000, Upper = 10000.
lower=1000
upper=10000

# Idnetify the divisors, n=6 and x=12.
n=6
x=12

# For every number represneted by i in the range from lower limit to upper limit.
for i in range(lower,upper+1):
# If i the current number is divisible by n (6) and not divisible by x (12) 
     if(i%n==0) and (i%x!=0):
# Print the number to the user.   
       print (i)  

# Reference: https://www.sanfoundry.com/python-program-print-numbers-range-divisible-given-number/
# Reference: https://www.w3resource.com/python-exercises/python-conditional-exercise-1.php
# Reference: Week 4 Loops https://web.microsoftstream.com/video/20963781-2aea-4302-ba73-5b8f327f4189
# Laura Brogan 	25/03/2019