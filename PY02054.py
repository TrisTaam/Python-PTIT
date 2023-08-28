n,m=map(int,input().split())
a=[]
for i in range(n):
    a.append([int(i) for i in input().split()])
b=[]
if n==m:
    b=a.copy()
elif n>m:
    k=n-m
    for i in range(n):
        if i%2==0 and i<=(n-m-1)*2:
            k-=1
            continue
        b.append(a[i])
else:
    k=m-n
    for i in range(n):
        c=[]
        for j in range(m):
            if j%2==1 and j<=(m-n)*2-1:
                continue
            c.append(a[i][j])
        b.append(c)
for i in b:
    for j in i:
        print(j,end=" ")
    print()