# Solution to Problem 6
# Ask the user to imput a sentence and output every second word.




#even_words = string.split()[::2]
#print(even_words, end =' ')



words = (input("Please enter").lower().split())

for word in words:
    if word % 2 == 0:
        print(word, end=' ') 

# "things to those who wait"


#count = 0
    # process line
#for word in n:
 #count+=1
#if count % 2 == 0:


    

#string = n
#even_words = string.split('input')[::2]
#print(n)

# Reference: https://stackoverflow.com/questions/54857129/write-a-program-that-takes-a-user-input-string-and-outputs-every-second-word
# Reference: https://www.programiz.com/python-programming/string
# Laura Brogan 