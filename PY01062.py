from math import sqrt

def nto(n):
    end=int(sqrt(n))
    for i in range(2,end+1):
        if n%i==0:
            return False
    return n>1

def res(s):
    if nto(len(s))==False:
        return False
    cnt=0
    for i in s:
        if nto(int(i)):
            cnt+=1
    return cnt>len(s)-cnt

t=int(input())
while t>0:
    s=input()
    print("YES" if res(s) else "NO")
    t-=1