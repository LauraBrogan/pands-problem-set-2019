# Solution to Problem 5
# Ask the user to Input a positive integer and output to the user whether or not the number is a prime number.

# y is asking the user to input a postive integer.
y = int(input("Please enter a positive integer: "))
# take input from the user if it is greather than or 
if y < 1:
    print("Unfortunately this is not a positive integer.") 
    quit()

# prime numbers are greater than 1
if y > 1:
   # check for factors
   for i in range(2,y):
       if (y % i) == 0:
           print(y,"is not a prime number.")
           break
   else:
       print("That is a prime number.")
       
# if input number is less than
# or equal to 1, it is not prime
#else:
   #print(num,"is not a prime number")

#  https://www.programiz.com/python-programming/examples/prime-number
# Laura Brogan