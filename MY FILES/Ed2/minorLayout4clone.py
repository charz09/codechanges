def addWhitespace(string): # this function adds whitespace to strings
	return(string.replace("", " ")[1: -1])
def removeWhitespace(string): # this function removes whitespace from strings
	newString = string.replace(" ", "")
	return newString
# single comment
def removeVowels(string): # this function removes vowels from strings
	newString = ""
	vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
	for x in string:
		if x in vowels:
			string = string.replace(x, "")
	return string
def reverseLine(string): # this function reverses a string
	newString = string[::-1]
	return newString
testString = "GeeeksforGeeks - A Computer Science Portal for Geeks"
print(addWhitespace(testString))
