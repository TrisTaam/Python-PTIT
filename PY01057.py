from math import sqrt

def nto(n):
    end=int(sqrt(n))
    for i in range(2,end+1):
        if n%i==0:
            return False
    return n>1

def res(s):
    for i in range(len(s)):
        if nto(i)^nto(int(s[i]))==1:
            return False
    return True

t=int(input())
while t>0:
    s=input()
    print("YES" if res(s) else "NO")
    t-=1