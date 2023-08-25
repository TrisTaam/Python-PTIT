def printx(x):
    for i in x:
        for j in i:
            print(j,end=" ")
        print()
    print()

dx=[-1,-1,-1,0,1,1,1,0]
dy=[-1,0,1,1,1,0,-1,-1]

n,m=map(int,input().split())
a=[]
for i in range(n):
    b=[int(j) for j in input().split()]
    a.append(b)
ans=0
b=[]
for i in range(n):
    c=[0 for j in range(m)]
    b.append(c)
for i in range(n):
    for j in range(m):
        if a[i][j]==-1:
            for z in range(8):
                x,y=i+dx[z],j+dy[z]
                if x>=0 and y>=0 and x<n and y<m and b[x][y]==0:
                    ans+=a[x][y]
                    b[x][y]=1
print(ans)