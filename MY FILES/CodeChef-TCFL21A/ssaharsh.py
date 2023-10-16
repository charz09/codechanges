t= int(input())

for i in range(t):
    K,M = map(int,input().split(" "))
    xarr=[int(ele) for ele in input().split(" ")]
    yarr=[int(ele) for ele in input().split(" ")]
    sum=0
    pxloc=0
    pyloc=0
    for i in range(K):
        sum = sum + abs(pxloc-xarr[i])
        sum = sum + abs(pyloc-yarr[i])
        pxloc=xarr[i]
        pyloc=yarr[i]
        
    if sum<M:
        print("YES")
        
    else:
        print("NO")
        