# Solution to Problem 5
# Ask the user to Input a positive integer and output to the user whether or not the number is a prime number.

# y is asking the user to input a postive integer.
y = int(input("Please enter a positive integer: "))
# Take input from the user if it is less than 0 display to user that this is not a positive interger and quit the programme.
if y < 1:
    print("Unfortunately this is not a positive integer.") 
    quit()
# If the user inputs 1, let them know this is not a prime number and quit
if y == 1:
    print("That is not a prime number.") 
    
# Prime numbers are greater than 1, if y is greater than 1
if y > 1:
   # check for factors if y is divisible by 2 it is not a prime number
   for i in range(2,y):
       if (y % i) == 0:
           print(y,"is not a prime number.")
           break
# Else it is divisible by 2 and it is a prime number. 
   else:
       print("That is a prime number.")
       
# Reference: https://www.programiz.com/python-programming/examples/prime-number
# Laura Brogan 25/03/2019