# cook your dish here
from sys import stdin, stdout
def arrin():
    return list(map(int, stdin.readline().split()))
def num1in():
    return int(stdin.readline())
def num2in():
    a, b = map(int, stdin.readline().split())
    return a, b
def num3in():
    a, b, c = map(int, stdin.readline().split())
    return a, b, c
def num4in():
    a, b, c, d = map(int, stdin.readline().split())
    return a, b, c, d
def num5in():
    a, b, c, d, e = map(int, stdin.readline().split())
    return a, b, c, d, e


t=num1in()
for test in range(t):
    k,m=num2in()
    x=arrin()
    y=arrin()
    coordinates=[[x[i],y[i]] for i in range(k)]
    px=0
    py=0
    dist=0
    tog=0
    ch=0
    while(tog<k):
        xi=coordinates[tog][0]
        yi=coordinates[tog][1]
        dist+= abs(xi-px)+abs(yi-py)
        px=xi
        py=yi
        tog+=1
        if(dist>=m):
            ch=1
            break
        
    if(ch==0):
        print("YES")
    else:
        print("NO")
        
        
        