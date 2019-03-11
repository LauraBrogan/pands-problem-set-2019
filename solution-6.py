# Solution to Problem 6
# Ask the user to imput a sentence and output every second word.


n = (input("Please enter a sentence: "))
#order using positional argument

count = 0
    # process line
for line in n:
 count+=1
if count % 2 == 0:
    print(n)

# Reference: https://www.programiz.com/python-programming/string
# Laura Brogan 