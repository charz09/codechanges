num = 130

# irrelevant stuff here:
sum = 0
for i in range(2, num):
	sum += i
print("sum = ",sum)

for i in range(2, num):
	if num % i  == 0:
		print(num,"is not a prime number")
		break
else:
	print(num,"is a prime number")
