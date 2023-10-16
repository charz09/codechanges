def prime_finder(n):
    number_range = set(range(n, 1, -1))
    primes_list = []
    while number_range:
        prime = number_range.pop()
        primes_list.append(prime)
        number_range.difference_update(set(range(prime*2, n+1, prime)))
    return primes_list
 
n = 130
primes_list = prime_finder(n)
print primes_list

if n in primes_list:
	print(n,"is a prime number")
else:
	print(n,"is not a prime number")
