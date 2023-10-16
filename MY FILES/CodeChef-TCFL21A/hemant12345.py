# cook your dish here
for i in range(int(input())):
    n,m=[int(x) for x in input().split()]
    X=[int(x) for x in input().split()]
    Y=[int(x) for x in input().split()]
    st_x=0
    st_y=0
    tot=0
    for j in range(n):
        dis=abs(X[j]-st_x)
        dis+=abs(Y[j]-st_y)
        st_y=Y[j]
        st_x=X[j]
        tot+=dis
    if tot<m:
        print("YES")
    else:
        print("NO")
        
    
