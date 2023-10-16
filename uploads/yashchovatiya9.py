t=int(input())
for i in range (t):
    n,m=map(int,input().split())
    l1=list(map(int,input().split()))
    l2=list(map(int,input().split()))
    x=0
    y=0
    cout=0
    for j in range (n):
        cout=cout+abs(x-l1[j])
        cout=cout+abs(y-l2[j])
        x=l1[j]
        y=l2[j]
    if(cout<m):
        print("YES")
    else:
        print("NO")
    
  
            