from math import sqrt
import array
import sys

N=2*10**6+1

a=array.array('i',[0]*N)
end=int(sqrt(N-1))
for i in range(2,end+1):
    if a[i]==0:
        a[i]=i
        for j in range(i*2,N,i):
            a[j]=i

for i in range(4,N):
    a[i]+=i if a[i]==0 else a[i//a[i]]

t=int(sys.stdin.readline())
ans=0
while t>0:
    n=int(sys.stdin.readline())
    ans+=a[n]
    t-=1
print(ans)