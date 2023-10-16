# cook your dish here
import math
for _ in range(int(input())):
    n,k=map(int, input().split())
    a=list(map(int, input().split()))
    b=list(map(int, input().split()))
    ans=0
    ans+=abs(a[0])+abs(b[0])
    for i in range(1,n):
        ans+=abs(a[i]-a[i-1])+abs(b[i]-b[i-1])
    if ans<k:
        print("YES")
    else:
        print("NO")
        
