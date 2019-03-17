# Solution to Problem 4
# 

# n is asking the user to input a postive integer.
n = int(input("Input a Positive Number: "))

# If the user inputs a negative number or a zero the programe displays "this is not a positive number" and ends the program.
if n <= 0:
    print("Unfortunately this is not a positive number.") 
    quit()

def collatz(n):
    print(n)
    #this will stop the program when it gets to one.
    while n != 1:
        if n % 2 == 0:
            n = n // 2
            print(n)
        else:
            n = n * 3 + 1
            print(n)
collatz (n)
# Reference https://stackoverflow.com/q/33324432
# Laura Brogan 