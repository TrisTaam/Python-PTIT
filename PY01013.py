from math import sqrt,gcd

def nto(n):
    end=int(sqrt(n))
    for i in range(2,end+1):
        if (n%i==0):
            return False
    return n>1

t=int(input())
while t>0:
    a,b=map(int,input().split())
    ucln=gcd(a,b)
    ans=sum(int(i) for i in str(ucln))
    print(f"YES" if nto(ans) else "NO")
    t-=1