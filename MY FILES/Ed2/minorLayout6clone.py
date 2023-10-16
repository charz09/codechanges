
numOfRows = 4

asciiVal = 65

for i in range(numOfRows):
	for j in range(i + 1):
		alphabet = chr(asciiVal)
		print(alphabet, end = " ")

	asciiVal += 1
	print("\n")

"""


multi-line comment


"""