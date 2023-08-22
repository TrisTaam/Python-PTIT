import sys
from math import sqrt

def nto(n):
    end=int(sqrt(n))
    for i in range(2,end+1):
        if n%i==0:
            return False
    return n>1

t=int(sys.stdin.readline())
while t>0:
    n=int(sys.stdin.readline())
    for i in range(n):
        j=int(str(i)[::-1])
        if i!=j and i<j and j<n:
            if nto(i) and nto(j):
                print(i,j,end=" ")
    print()
    t-=1