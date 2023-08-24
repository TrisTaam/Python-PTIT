a="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

t=int(input())
while t>0:
    n,k=map(int,input().split())
    s=""
    while n>0:
        s=a[n%k]+s
        n//=k
    print(s)
    t-=1