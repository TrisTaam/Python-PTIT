from math import sqrt

def nto(n):
    end=int(sqrt(n))
    for i in range(2,end+1):
        if n%i==0:
            return False
    return True

n=int(input())
a=[int(i) for i in input().split()]
b={}
for i in a:
    if nto(i)==True:
        if i in b:
            b[i]+=1
        else:
            b[i]=1
for i,j in b.items():
    print(i,j)