import math

def quadratic(d, e, f):
	dis = e * e - 4 * d * f
	sqrt_value = math.sqrt(abs(dis))

	if dis > 0:
		print("Real and different roots.")
		print((-e + sqrt_value)/(2 * d))
		print((-e - sqrt_value)/(2 * d))
	elif dis == 0:
		print("Real and same roots.")
		print(-e / (2 * d))
	else:
		print("Complex Roots")
		print(- e / (2 * d), " + i", sqrt_value) 
		print(- e / (2 * d), " - i", sqrt_value)

d = 10
e = 12
f = -1

if d == 0:
	print("Input correct quadratic equation")
else:
	quadratic(d, e, f)
