# cook your dish here
for i in range(int(input())):
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=list(map(int,input().split()))
    d=0
    x=0
    y=0
    for i in range(len(b)):
        d=d+abs(b[i]-x)
        d=d+abs(c[i]-y)
        x=b[i]
        y=c[i]
    if d<a[1]:
        print("YES")
    else:
        print("NO")