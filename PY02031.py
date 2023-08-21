from math import sqrt

def nto(n):
    end=int(sqrt(n))
    for i in range(2,end+1):
        if n%i==0:
            return False
    return n>1

n,m=map(int,input().split())
a=[]
for i in range(n):
    b=[int(i) for i in input().split()]
    a.append(b)
for i in a:
    for j in i:
        print(1 if nto(j) else 0,end=" ")
    print()