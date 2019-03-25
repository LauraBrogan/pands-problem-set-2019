# Solution to Problem 6
# Ask the user to imput a sentence and output every second word.

user = input("Please Enter a Sentence:")
even_words = user.split(' ')
print(even_words[::2], end ="")



# Reference: https://stackoverflow.com/questions/54857129/write-a-program-that-takes-a-user-input-string-and-outputs-every-second-word
# Reference: https://www.programiz.com/python-programming/string
# Laura Brogan 