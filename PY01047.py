from math import sqrt

def nto(n):
    end=int(sqrt(n))
    for i in range(2,end+1):
        if n%i==0:
            return False
    return n>1

t=int(input())
while t>0:
    s=input()
    n=int(s) if len(s)<=4 else int(s[-4:])
    print("YES" if nto(n) else "NO")
    t-=1