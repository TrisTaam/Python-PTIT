A=1005

t=int(input())
while t>0:
    n=int(input())
    a=[int(i) for i in input().split()]
    b=[False]*A
    mina=A
    maxa=0
    for i in a:
        b[i]=True
        mina=min(mina,i)
        maxa=max(maxa,i)
    ans=0
    for i in range(mina,maxa+1):
        if not(b[i]):
            ans+=1
    print(ans)
    t-=1