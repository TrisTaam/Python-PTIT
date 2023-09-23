t=int(input())
while t>0:
    n,p=map(int,input().split())
    ans=0
    while n>0:
        ans+=n//p
        n//=p
    print(ans)
    t-=1