from math import sqrt

def nto(n):
    end=int(sqrt(n))
    for i in range(2,end+1):
        if n%i==0:
            return False
    return True

n=int(input())
a=[]
s=0
for i in input().split():
    if int(i) not in a:
        a.append(int(i))
        s+=int(i)
s1=0
pos=-1
for i in range(len(a)):
    s1+=a[i]
    if nto(s1) and nto(s-s1):
        pos=i
        break
print(pos if pos>-1 else "NOT FOUND")