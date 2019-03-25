# Solution to Problem 3
# Print all numbers between 1,000 and 10,000 that are divisible by 6 but not 12.

lower=1000
upper=10000
n=6
x=12
for i in range(lower,upper+1):
     if(i%n==0) and (i%12!=0):
       print(i)     
#https://www.sanfoundry.com/python-program-print-numbers-range-divisible-given-number/

	