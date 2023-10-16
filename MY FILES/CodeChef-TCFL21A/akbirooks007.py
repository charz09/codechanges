for _ in range(int(input())):
    k, m = map(int, input().strip().split(" "))
    x = list(map(int, input().strip().split(" ")))
    y = list(map(int, input().strip().split(" ")))
    xc = 0
    yc = 0
    s = True
    l = len(x)
    for i in range(l):
        p = abs(x[i] - xc) + abs(y[i] - yc)
        if m > p:
            m = m - p
            xc = x[i]
            yc = y[i]
        else:
            s = False
            break
    if s:
        print("YES")
    else:
        print("NO")
    