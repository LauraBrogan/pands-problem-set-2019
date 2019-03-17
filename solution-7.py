# Solution to Problem 7
# Ask the user to Input any positive floating point number and output an approximation of its aquare root..
import math

# n is asking the user to input a postive number
n = float(input("Input a Positive Floating Point Number: "))

# If the user inputs a negative number or a zero the programe displays "this is not a positive number" and ends the program
total = 0.0 

if n <= 0.0:
    print("Unfortunately this is not a positive number.") 
    quit()

# If the user inputs a postive number the program runs and sums all of the numbers between one and that number and then displays the total.   
while n > 0.0:
#Verbatium lines 18-20 inc from reference 1 below
    n = float(n)
    number_sqrt = n ** 0.5
    print("Square Root of Floating point number %0.2f is %0.2f" %(n, number_sqrt))
    quit()


# Reference 1 https://codescracker.com/python/program/python-program-find-square-root.htm
# Laura Brogan 
