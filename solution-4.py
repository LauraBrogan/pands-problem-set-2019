# Solution to Problem 4
# 

# n is asking the user to input a postive integer.
i = int(input("Input a Positive Number: "))

# If the user inputs a negative number or a zero the programe displays "this is not a positive number" and ends the program.
if i <= 0:
    print("Unfortunately this is not a positive number.") 
    quit()

# If the user inputs a postive number greater than zero the program runs.   
if i > 0:
    while i !=1:
     def collatz(i):
        if i % 2 == 0:
         print(i // 2)
         return i // 2

        elif i % 2 == 1:
         result = 3 * i + 1
         print(result)
       




      #  while i != 1:
          # if i % 2==0:
           #  i = (i//2)
            #print(number)
           # return (print(int(i)))

           # while i % 2==1:
          #   i = (3*i+1) 
            #print(number)
           # return (print(int(i)))
quit()  
        #continue


# 
# Reference 
# Laura Brogan 