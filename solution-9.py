# Solution to Problem 9
# Program to read a text file from user input and output every second line. 

# Ask the user to open text file, this will be the user input. 
userinput = input("Please open text file:") 

# The the "With" statement, simplifies the handling of opening text file "Staunton" and will automatically close the file.
# We open file as F and for every line in F,

with open(userinput,'r') as f:
# We use the built in enumberate function to count the lines.
       for x, line in enumerate(f):
 # For every line that is divisable by two starting at line 1.
          if x % 2 == 1:
 # We print that line therefore displaying every second line of the text file to the user. 
            print(line)
      

# Reference: https://www.daniweb.com/programming/software-development/threads/283568/delete-every-second-line
# Reference: https://stackoverflow.com/a/30551984
# Reference: https://www.google.ie/search?ei=x9CGXMnRBo2W1fAP8qipmA0&q=python+ask+user+to+input+text+file+to+open&oq=python+ask+user+to+input+text+file+to+open&gs_l=psy-ab.3...9189.14861..15111...0.0..0.240.3820.23j8j3......0....1..gws-wiz.......0i71j0j0i22i30j33i22i29i30j33i21j33i160.FNIkRLrH8TI#kpvalbx=1
# Reference: Week 7 Lecture https://web.microsoftstream.com/video/72484dfc-1b50-4223-8039-bd6a69cab573
# Laura Brogan 16/03/19