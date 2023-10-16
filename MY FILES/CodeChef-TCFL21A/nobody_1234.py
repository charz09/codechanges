# cook your dish here
for _ in range(int(input())):
    m,k=map(int,input().split())
    x=list(map(int,input().split()))
    y=list(map(int,input().split()))
    a=0
    b=0
    ans=0
    for i in range(m):
        ans+=abs(a-x[i])+abs(b-y[i])
        a=x[i]
        b=y[i]
    if(ans<k):
        print("YES")
    else:
        print("NO")