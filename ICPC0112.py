import sys
from math import sqrt

N=10**6+1
a=[True]*N
a[0]=a[1]=False
end=int(sqrt(N-1))
for i in range(2,end+1):
    if a[i]:
        for j in range(i*i,N,i):
            a[j]=False
b=[i for i in range(N) if a[i]]

t=int(sys.stdin.readline())
while t>0:
    n=int(sys.stdin.readline())
    ans=0
    for i in b:
        if i+6>=n:
            break
        if (a[i+2] or a[i+4]) and a[i+6]:
            ans+=1
    print(ans)
    t-=1