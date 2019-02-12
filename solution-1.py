# Solution to Problem 1
# Input any positive integer and output the sum of all numbers between one and that numbers

n = int(input("Input a Positive Number: "))
# n is asking the user to input a postive number

if n < 0:
     print("Unfortunately this is not a positive integer") 
quit() 


sum = 0
while (n>0):
    sum += n
    n-= 1

print("This is the Sum", sum)


    #if the user inputs a negative number the programe displays "this is not a positive integer" and ends the program
    #if the user inputs a postive number the program runs and sums all of the numbers between one and that number and then displays it

