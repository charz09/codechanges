def reverseLine(string):
	newString = string[::-1]
	return newString

def removeVowels(string):
	newString = ""
	vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
	for x in string:
		if x in vowels:
			string = string.replace(x, "")
	return string

def removeWhitespace(string):
	newString = string.replace(" ", "")
	return newString

def addWhitespace(string):
	return(string.replace("", " ")[1: -1])

testString = "GeeeksforGeeks - A Computer Science Portal for Geeks"

print(addWhitespace(testString))
