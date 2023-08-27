from math import sqrt

def nto(n):
    end=int(sqrt(n))
    for i in range(2,end+1):
        if n%i==0:
            return False
    return n>1

n=int(input())
a=[int(i) for i in input().split()]
ans=0
for i in a:
    x=i
    while not(nto(x)):
        x+=1
    cnt=x-i
    x=i
    while not(nto(x)):
        x-=1
    cnt=min(cnt,i-x)
    ans=max(ans,cnt)
print(ans)