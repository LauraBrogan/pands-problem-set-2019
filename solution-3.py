# Solution to Problem 3
# Print all numbers between 1,000 and 10,000 that are divisible by 6 but not 12.


#lower=1000
#upper=10000
#n=6
#for i in range(lower,upper):
   # if (i%n==0):
      #  print(i)
      #  and 



#nl=[]
#for x in range(1000, 10000):
 #if (x%6==0):
   #     nl.append(str(x))
#print (','.join(nl))
#while (x%12) !=0:
  #   nl.append(str(x))
#print (','.join(nl))

#quit()

#Reference: https://www.w3resource.com/python-exercises/python-conditional-exercise-1.php

# Laura Brogan


lower=1000
upper=10000
for i in range(lower,upper+1):
   if (i%6==0):
      while(i%12) !=0:
       print (i)