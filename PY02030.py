from math import sqrt

def nto(n):
    end=int(sqrt(n))
    for i in range(2,end+1):
        if n%i==0:
            return False
    return n>1

n=int(input())
a=[int(i) for i in input().split()]
b=[]
s=0
for i in a:
    if i not in b:
        b.append(i)
        s+=i
s1=0
ans=-1
for i in range(len(b)):
    s1+=b[i]
    if nto(s1) and nto(s-s1):
        ans=i
        break
print(ans if ans!=-1 else "NOT FOUND")