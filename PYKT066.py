from math import gcd

t=int(input())
while t>0:
    n,k=map(int,input().split())
    a=[]
    while True:
        x=[int(i) for i in input().split()]
        a+=x
        if (len(a)==n):
            break
    ans=10**9
    for i in range(len(a)):
        if a[i]%k==0:
            tmp=a[i]
            for j in range(i,len(a)):
                tmp=gcd(tmp,a[j])
                if tmp<k:
                    break
                if tmp==k:
                    ans=min(ans,j-i+1)
                    break
    print(ans if ans!=10**9 else -1)
    t-=1