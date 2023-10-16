# cook your dish here
t = int(input().rstrip())
for _ in range(t):
       (n, k) = list(map(int, input().rstrip().split(" ")))
       list1 = list(map(int, input().rstrip().split(" ")))
       list2 = list(map(int, input().rstrip().split(" ")))
       sum1 = 0
       x = 0
       y = 0
       for i in range(n):
              sum1 += abs(list1[i]-x)+abs(list2[i]-y)
              x = list1[i]
              y = list2[i]
       if sum1 < k:
              print("YES")
       else:
              print("NO")
