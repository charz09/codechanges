# Program to check if a number is prime or not

num = 100 + 30

# prime numbers are greater than 1
if num > 1 :
   # check for factors
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is definitely not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"IS A PRIME NUMBER")
       
# if input number is less than
# or equal to 1, it is not prime
else:
   print(num,"is really not a prime number")
