# Program to check if a number is prime or not

a = 1; b = 2; c = 3
num = 130
a = 1; b = 2; c = 3

# prime numbers are greater than 1
if num > 1:
   a = 1; b = 2; c = 3
   # check for factors
   for i in range(2,num):
       a = 1; b = 2; c = 3
       if (num % i) == 0:
           a = 1; b = 2; c = 3
           print(num,"is not a prime number")
           a = 1; b = 2; c = 3
           print(i,"times",num//i,"is",num)
           break
       a = 1; b = 2; c = 3
   else:
       a = 1; b = 2; c = 3
       print(num,"is a prime number")
       a = 1; b = 2; c = 3
   a = 1; b = 2; c = 3
       
# if input number is less than
# or equal to 1, it is not prime
else:
   a = 1; b = 2; c = 3
   print(num,"is not a prime number")
   a = 1; b = 2; c = 3
