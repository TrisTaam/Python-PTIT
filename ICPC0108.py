import sys

t=int(sys.stdin.readline())
while t>0:
    n=int(sys.stdin.readline())
    a=sorted([int(i) for i in sys.stdin.readline().split()])
    ans=0
    for i in range(n-2):
        l=i+1
        r=n-1
        while l<r:
            if a[i]+a[l]+a[r]==0:
                ans+=1
                l+=1
            elif a[i]+a[l]+a[r]<0:
                l+=1
            else:
                r-=1
    print(ans)
    t-=1