t=int(input())
while t>0:
    n=int(input())
    a=[]
    b=[]
    for i in range(n):
        x,y=map(float,input().split())
        a.append(x)
        b.append(y)
    c=[]
    for i in range(n):
        c.append(1)
        for j in range(0,i):
            if a[j]<a[i] and b[j]>b[i]:
                c[i]=max(c[i],c[j]+1)
    print(max(c))
    t-=1