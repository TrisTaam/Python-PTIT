import sys
from queue import Queue
import bisect as bs

a=Queue()
a.put(1)
b=[]
c=[2,3,5]
d={1:1}
while not(a.empty()):
    x=a.get()
    b.append(x)
    for i in c:
        if x*i<=10**18 and x*i not in d:
            a.put(x*i)
            d[x*i]=1
b.sort()

t=int(sys.stdin.readline())
while t>0:
    n=int(sys.stdin.readline())
    e=bs.bisect_left(b,n)
    print(e+1 if b[e]==n else "Not in sequence")
    t-=1