from math import sqrt

def nto(n):
    end=int(sqrt(n))
    for i in range(2,end+1):
        if n%i==0:
            return False
    return n>1

def eulerTotient(n):
    end=int(sqrt(n))
    ans=n
    for i in range(2,end+1):
        if n%i==0:
            ans*=(1-1/i)
            while n%i==0:
                n/=i
    if n>1:ans*=(1-1/n)
    return int(ans)

t=int(input())
while t>0:
    n=int(input())
    print(f"YES" if nto(eulerTotient(n))==True else "NO")
    t-=1