
def fib(n):
	if n<=1:
		return n
	return fib(n-1) + fib(n-2)
# single line comment
print(fib(16))