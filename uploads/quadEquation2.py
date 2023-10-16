import math

quad = 89

def quadraticEquation(a, b, c):
	dis = b * b - 4 * a * c
	sqrt_val = math.sqrt(abs(dis))

	if dis > 0:
		print("Real and different roots.")
		print((-b + sqrt_val)/(2 * a))
		print((-b - sqrt_val)/(2 * a))
	elif dis == 0:
		print("Real and same roots.")
		print(-b / (2 * a))
	else:
		print("Complex Roots")
		print(- b / (2 * a), " + i", sqrt_val) 
		print(- b / (2 * a), " - i", sqrt_val)

a = 10
b = 12
c = -1
d = 1
e = 2
f = 3

if a == 0:
	print("Input correct quadratic equation")
else:
	quadraticEquation(a, b, c)
