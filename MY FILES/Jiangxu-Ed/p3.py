# Program to check if a number is prime or not

testNumber = 130

# prime numbers are greater than 1
if testNumber > 1:
   # check for factors
   for i in range(2,testNumber):
       if (testNumber % i) == 0:
           print(testNumber,"is not a prime number")
           print(i,"times",testNumber//i,"is",testNumber)
           break
   else:
       print(testNumber,"is a prime number")
       
# if input number is less than
# or equal to 1, it is not prime
else:
   print(testNumber,"is not a prime number")
