t=int(input())
while t>0:
    n,m=map(int,input().split())
    a=[]
    for i in range(n):
        b=[int(i) for i in input().split()]
        a.append(b)
    b=[]
    for i in range(3):
        c=[int(i) for i in input().split()]
        b.append(c)
    ans=0
    for i in range(n-2):
        for j in range(m-2):
            for z in range(3):
                for p in range(3):
                    ans+=a[i+z][j+p]*b[z][p]
    print(ans)
    t-=1