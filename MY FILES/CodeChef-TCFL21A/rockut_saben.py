try:
    for _ in range(int(input())):
        k,m = list(map(int, input().split()))
        x = list(map(int, input().split()))
        y = list(map(int, input().split()))
        moves = 0
        current = [0,0]
        for i in range(k):
            moves += abs(current[0]-x[i]) + abs(current[1]-y[i])
            current=[x[i],y[i]]
        if(moves<m):
            print("YES")
        else:
            print("NO")
except:
    pass