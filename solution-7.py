# Solution to Problem 7
# Ask the user to Input any positive floating point number and output an approximation of its square root.
# To start I import the Python math module.
import math

# n is asking the user to input a postive floating point number
n = float(input("Input a Positive Floating Point Number: "))

# If the user inputs a negative number or a zero the programe displays "this is not a positive number" and ends the program.
if n <= 0.0:
    print("Unfortunately this is not a positive number.") 
    quit()

# If the user inputs a postive number greater than zero the program runs.   
while n > 0.0:
# Verbatium lines 18-22 inc from reference 1 below.
# n is the number the user inputs as a floating point number.
    n = float(n)
# The built in function calculates the square root of the inputted number.
    number_sqrt = n ** 0.5
# Displays the number we are finding the root of with 1 decimal place the square root with 1 decimal place.
    print("The Square Root of Floating point number %0.1f is approx %0.1f" %(n, number_sqrt))
# Closes the program
    quit()

# Used solution 1 to 2019 problem set as the base for this answer.
# Reference 1 https://codescracker.com/python/program/python-program-find-square-root.htm
# Laura Brogan 17/03/2019
