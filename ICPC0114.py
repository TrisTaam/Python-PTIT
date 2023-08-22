import sys
from math import sqrt

def nto(n):
    end=int(sqrt(n))
    for i in range(2,end+1):
        if n%i==0:
            return False
    return n>1

def res(n):
    if not nto(n):
        return False
    cnt=0
    n1=0
    while n>0:
        a=n%10
        if not nto(a):
            return False
        cnt+=a
        n1=n1*10+a
        n//=10
    return nto(n1) and nto(cnt)

t=int(sys.stdin.readline())
while t>0:
    n=int(sys.stdin.readline())
    print("Yes" if res(n) else "No")
    t-=1