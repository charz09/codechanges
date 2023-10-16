print("Enter a year: ")
year = input()
num = 0
num1 = 1
num2 = 2
if (year % 4) == 0:
	if (year % 100) == 0:
		if (year % 400) == 0:
			print(year + "is a leap year")
		else:
			print(year + "is not a leap year")
	else:
		print(year + "is a leap year")
else:
	print(year + "is not a leap year")

def ifCheck(inputInt):
	if inputInt == 0:
		pass
	else:
		print("The input is not a 0.")