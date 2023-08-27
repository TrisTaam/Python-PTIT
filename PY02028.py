from math import sqrt

def nto(n):
    end=int(sqrt(n))
    for i in range(2,end+1):
        if n%i==0:
            return False
    return n>1

n=int(input())
a=[int(i) for i in input().split()]
b=[]
c=[]
for i in range(len(a)):
    if nto(a[i]):
        b.append(a[i])
        c.append(i)
b.sort()
for i in range(len(c)):
    a[c[i]]=b[i]
for i in a:
    print(i,end=" ")