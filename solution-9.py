# Solution to Problem 9
# Program to read a text file and output every second line. 

userinput = input("Please open text file:") 

# The the "With" statement, simplifies the handling of opening text file "Staunton" and will automatically close the file.
# We open file as F and count for every line in F, if the line is divisible by 2 we print the line. 

with open('userinput','r') as f:
    count = 0
    # process line
    for line in f:
      count+=1
    if count % 2 == 0:
       print(Line)




# Reference: https://stackoverflow.com/a/30551984
# Reference: Week 7 Lecture https://web.microsoftstream.com/video/72484dfc-1b50-4223-8039-bd6a69cab573
# Laura Brogan 11/03/19