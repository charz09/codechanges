import itertools 
for i in range(int(input())):
    k,m=map(int,input().split())
    x=list(map(int,input().split()))
    y=list(map(int,input().split()))
    count=0
    pre_x=0
    pre_y=0
    for (i,j) in zip(x,y):
        dist=abs(i-pre_x)+abs(j-pre_y)
        count+=dist
        pre_x=i
        pre_y=j
    if count<m:
        print("YES")
    else:
        print("NO")
        