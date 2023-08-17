from math import sqrt

t=int(input())
while t>0:
    n=int(input())
    print(1,end="")
    i=2
    while i*i<=n:
        cnt=0
        while n%i==0:
            cnt+=1
            n//=i
        if cnt>0:
            print(f" * {i}^{cnt}",end="")
        i+=1
    if n>1:
        print(f" * {n}^1",end="")
    print()
    t-=1