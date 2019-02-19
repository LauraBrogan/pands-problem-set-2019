# Solution to Problem 1
# Input any positive integer and output the sum of all numbers between one and that numbers

n = int(input("Input a Positive Number: "))
# n is asking the user to input a postive number

total = 0

if n < 0:
     print("Unfortunately this is not a positive integer") 
quit() 

while n > 0:
    total = total + n
    n = n - 1
   
print(total)



    #if the user inputs a negative number the programe displays "this is not a positive integer" and ends the program
    #if the user inputs a postive number the program runs and sums all of the numbers between one and that number and then displays it

