# Solution to Problem 1
# Input any positive integer and output the sum of all numbers between one and that numbers

n = int(input("Input a number: "))
# n is asking the use to input a postive number


if n > 1: sum_num = n + 1 
print (sum_num)
    #if the user inputs a postive number the program runs and sums all of the number between one and that number and then displays it


if n < 1: print ("Unfortunately this is not a positive integer")
    #if the user inputs a negative number the programe displays "this is not a positive integer"
