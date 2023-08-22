import sys

t=int(sys.stdin.readline())
while t>0:
    n,k=map(int,sys.stdin.readline().split())
    a=[int(i) for i in sys.stdin.readline().split()]
    k%=n
    for i in range(k,n):
        print(a[i],end=" ")
    for i in range(k):
        print(a[i],end=" ")
    print()
    t-=1