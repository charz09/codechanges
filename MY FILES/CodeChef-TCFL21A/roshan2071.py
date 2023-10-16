for i in range(int(input())):
 s0,c=[int(i) for i in input().split()],0
 n,k=s0
 first=[int(i) for i in input().split()]
 second=[int(i) for i in input().split()]
 lx=list(zip(first ,second ))
 lx.insert(0,(0,0))
 for i in range (1,len(lx)):
  c+=abs(lx[i][0]-lx[i-1][0])+abs(lx[i][1]-lx[i-1][1])
 r='YES' if c<k else 'NO'
 print (r)