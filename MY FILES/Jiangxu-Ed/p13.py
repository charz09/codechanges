## Dependencies
from functools import reduce

## The Data
n=130

n = n+1

## The One-Liner
primes = reduce(lambda r, x: r - set(range(x**2, n, x)) if x in r else r, range(2, int(n**0.5) + 1), set(range(2,n)))

if n-1 in primes:
	print(n-1,"is a prime number")
else:
	print(n-1,"is not a prime number")
