
for _ in range(int(input())):
    k,m = map(int,input().split())
    x = map(int,input().split())
    y = map(int,input().split())
    ans = last = 0
    for i in x:
        ans+=abs(last-i)
        last=i
    last=0
    for i in y:
        ans+=abs(last-i)
        last=i
    if ans<m:
        print('YES')
    else:
        print('NO')