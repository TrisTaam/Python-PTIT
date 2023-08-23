t=int(input())
a="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
while t>0:
    n,k=map(int,input().split())
    ans=""
    while n>0:
        ans=a[n%k]+ans
        n//=k
    print(ans)
    t-=1