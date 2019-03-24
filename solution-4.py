# Solution to Problem 4
# 

# n is asking the user to input a postive integer.
n = int(input("Input a Positive Integer: "))

# If the user inputs a negative number or a zero the programe displays "this is not a positive number" and ends the program.
if n <= 0:
    print("Unfortunately this is not a positive Integer.") 
    quit()

def collatz(n, sep = ", "):
    print(n, sep = ", ")
    #this will stop the program when it gets to one.
    while n != 1:
        if n % 2 == 0:
            n = n // 2
            print(n, sep = ", ")
        else:
            n = n * 3 + 1
        print (n) (sep = ”, ” )
collatz (n)
# Reference https://stackoverflow.com/q/33324432
# Laura Brogan 