# Solution to Problem 4
# Ask user to input any positive integer and outpts the successive valuses of the following calculation. 
# At each step calcuate the next value by taking the current value and, it is is even, divide it by two.
# But is if is odd, multiply it by thhree and add one.
# End program if the current value is one. 

# n is asking the user to input a postive integer.
n = int(input("Input a Positive Integer: "))

# If the user inputs a negative number or a zero the programe displays "this is not a positive number" and ends the program.
if n <= 0:
    print("Unfortunately this is not a positive Integer.") 
    quit()
# The Collatz conjecture is a conjecture that a particular sequence always reaches 1. 
# The sequence is defined as: start with a number n. 
# Verbatium from her to the end https://stackoverflow.com/q/33324432.
def collatz(n):
    print(n)
#This will stop the program when it gets to one.
    while n != 1:
# If The next number in the sequence is even n is divided by 2 and print that number.
        if n % 2 == 0:
            n = n // 2
            print(n)
# If n is odd we triple n and add  1 and print that number
        else:
            n = n * 3 + 1
            print(n)
collatz(n)

# Reference https://stackoverflow.com/q/33324432
# Laura Brogan 25/03/19
