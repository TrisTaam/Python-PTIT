import re

def res(s):
    if s=="":
        return False
    for i in s:
        if not(i.isalpha()) and not(i.isdigit()):
            return False
    return True

t=int(input())
b={}
while t>0:
    a=re.split(r"[ ,.?!:;()-/]",input().lower())
    for i in a:
        if res(i):
            if i in b:
                b[i]+=1
            else:
                b[i]=1
    t-=1
c=[]
for i,j in b.items():
    c.append((i,j))
c.sort(key=lambda x:(-x[1],x[0]))
for i,j in c:
    print(i,j)