#!/usr/bin/env/
def findFactors(input):
	for i in range(1,input+1):
		if input%i==0:
			print(i)

test=500
# single comment
findFactors(test)