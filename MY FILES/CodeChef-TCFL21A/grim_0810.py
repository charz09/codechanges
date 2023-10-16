for _ in range(int(input())):
    k, m = map(int, input().split())
    x_cords = list(map(int, input().split()))
    y_cords = list(map(int, input().split()))
    x_cords.insert(0, 0)
    y_cords.insert(0, 0)
    steps = 0
    for i in range(k):
        steps += abs(x_cords[i+1] - x_cords[i])
    for i in range(k):
        steps += abs(y_cords[i+1] - y_cords[i])
    print('YES') if steps < m else print('NO')
