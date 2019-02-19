# Solution to Problem 1
# Input any positive integer and output the sum of all numbers between one and that numbers

n = int(input("Input a Positive Number: "))
# n is asking the user to input a postive number

total = 0 

if n <= 0:
    print("Unfortunately this is not a positive integer.") 
    quit()
# If the user inputs a negative number of a zero the programe displays "this is not a positive integer" and ends the program
    
while n > 0:
    total = total + n
    n = n - 1
print(total,"This is the sum of all the numbers between one and the interger inputted above.")

# If the user inputs a postive number the program runs and sums all of the numbers between one and that number and then displays the total.

# Laura Brogan 19/02/2019

