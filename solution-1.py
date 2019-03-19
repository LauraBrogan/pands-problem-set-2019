# Solution to Problem 1
# Ask the user to Input any positive integer and output the sum of all numbers between one and that number.


# n is asking the user to input a postive integer.
n = int(input("Input a Positive Integer: "))

# If the user inputs a negative number or a zero the programe displays "this is not a positive integer" and ends the program.
total = 0 
if n <= 0:
    print("Unfortunately this is not a Positive Integer.") 
    quit()

# If the user inputs a postive number greater than zero the program runs.
# It sums all of the numbers between one and that number.   
while n > 0:
    total = total + n
    n = n - 1
# The answer is then displayed to the user with an explanation.
print(total,"This is the sum of all the numbers between one and the interger inputted above.")

# Used Class Tutorial for Factorial Problem as base for creation of the above. 
# Reference: https://stackoverflow.com/questions/50012895/pythonwrite-a-program-that-keeps-reading-positive-numbers-from-the-user
# Laura Brogan 19/02/2019