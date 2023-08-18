from math import sqrt

def nto(n):
    end=int(sqrt(n))
    for i in range(2,end+1):
        if n%i==0:
            return False
    return n>1

def res(s):
    ans=0
    for i in range(len(s)):
        if (i+int(s[i]))%2==1:
            return False
        ans+=int(s[i])
    return nto(ans)

t=int(input())
while t>0:
    s=input()
    print("YES" if res(s) else "NO")
    t-=1