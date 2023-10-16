"""
-> Author  : Om Anshuman   #
-> About   : IT Fresher	   #
-> Insti   : VIT, Vellore  #
-> Created : 25.04.2021    #
"""
"""
from sys import stdin, stdout
import math
from functools import reduce
import statistics
import numpy as np
import itertools
import sys
"""

def prog_name():
    k,m = map(int,input().split())
    x_co = list(map(int,input().split()))
    y_co = list(map(int,input().split()))
    final = []
    for x in range(len(x_co)):
        final.append([x_co[x],y_co[x]])
    steps = 0
    i = [0,0]
    for y in range(len(final)):
        steps += (abs(i[0]-final[y][0])+abs(i[1]-final[y][1]))  
        i = final[y]
    if steps<m:
        print("YES")
    else:print("NO")
t = int(input())
for unique in range(t):
	prog_name()