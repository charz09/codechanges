# cook your dish here
for _ in range(int(input())):
    k,m=map(int,input().split())
    X=list(map(int,input().split()))
    Y=list(map(int,input().split()))
    count=0
    i,j=0,0
    for itr in range(k):
        count+=abs(X[itr]-i)+abs(Y[itr]-j)
        i=X[itr]
        j=Y[itr]
    # print(count)
    if count>=m:print("NO")
    else:print("YES")
    