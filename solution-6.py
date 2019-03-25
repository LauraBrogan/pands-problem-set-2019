# Solution to Problem 6
# Ask the user to imput a sentence and output every second word.

user = input("Please Enter a Sentence:")
even = user.split(' ')[::2]
display = " ".join(even)
print(display)



# Reference: https://stackoverflow.com/questions/54857129/write-a-program-that-takes-a-user-input-string-and-outputs-every-second-word
# Reference: https://www.programiz.com/python-programming/string
# Laura Brogan 

