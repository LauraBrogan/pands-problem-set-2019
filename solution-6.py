# Solution to Problem 6
# Ask the user to input a sentence and output every second word.

# User is the sentence the user inputs into the program. 
user = input("Please Enter a Sentence:")

# This splits the users input into string called even of every second word.
even = user.split(' ')[::2]

# Then we join the split back together with just the even works and call it display.
display = " ".join(even)

# This diplays every second word in the sentence to the user. 
print(display)

# Reference: https://stackoverflow.com/questions/54857129/write-a-program-that-takes-a-user-input-string-and-outputs-every-second-word
# Reference: https://www.programiz.com/python-programming/string
# Reference: https://www.hackerrank.com/challenges/python-string-split-and-join/problem
# Laura Brogan 25/03/2019

