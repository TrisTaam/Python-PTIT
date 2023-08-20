from math import gcd

n=int(input())
a=sorted([int(x) for x in input().split()])
b=[]
for i in range(n-1):
    for j in range(i+1,n):
        if gcd(a[i],a[j])==1:
            b.append((a[i],a[j]))
for i,j in b:
    print(i,j)