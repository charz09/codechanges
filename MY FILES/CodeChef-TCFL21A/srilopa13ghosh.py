# cook your dish here
t= int(input())
while t>0:
    k,m=map(int, input().split())
#    print(k, m)
    x=list(map(int, input().split()))
#    print(x)
    y=list(map(int, input().split()))
    x1=abs(0 - x[0])
    y1= abs(0 - y[0])
    s=x1+y1
    #print(s)
    for i in range(1,k):
        s += abs(x[i-1] - x[i])
        s += abs(y[i-1] - y[i])
        #print(s)
        
    #print(s) 
    if(s<m):
        print("YES")
    else:
        print("NO")
    t=t-1
