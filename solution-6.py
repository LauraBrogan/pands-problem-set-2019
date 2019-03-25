# Solution to Problem 6
# Ask the user to imput a sentence and output every second word.

#user = input("Please Enter a Sentence:")
#even_words = user.split[::2]
#print(even_words)


# Reference: https://stackoverflow.com/questions/54857129/write-a-program-that-takes-a-user-input-string-and-outputs-every-second-word
# Reference: https://www.programiz.com/python-programming/string
# Laura Brogan 

sentenceInput=(input ("Please enter sentence: "))

# Function for deleting every 2nd word
def wordDelete(sentence):

    # Splitting sentence into pieces by thinking they're seperated by space.
    # Comma and other signs are kept.
    sentenceList = sentence.split(" ")

    # Checking if sentence contains more than 1 word seperated and only then remove the word
  #  if len(sentenceList) > 1:
    sentenceList.remove(sentenceList[::2])

    # Re-joining sentence
    droppedSentence = ' '.join(sentenceList)

    # Returning the result
    return droppedSentence

    print(wordDelete(sentenceInput))