# Solution to Problem 1
# Input any positive integer and output the sum of all numbers between one and that numbers

n = int(input("Input a number: "))
# n is asking the user to input a postive number

if n < 0: print ("Unfortunately this is not a positive integer") 
quit () 

elif n > 0:
    pass sum_num = (n * (n + 1)) /2
    
print (sum_num)


    #if the user inputs a negative number the programe displays "this is not a positive integer" and ends the program
    #if the user inputs a postive number the program runs and sums all of the numbers between one and that number and then displays it

