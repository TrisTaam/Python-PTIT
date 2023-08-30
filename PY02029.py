n,m=map(int,input().split())
a=[int(i)-1 for i in input().split()]
b=[0]*m
for i in a:
    b[i]+=1
max1=max(b)
max2=0
for i in b:
    if max2<i and i<max1:
        max2=i
if max2==0:
    print("NONE")
else:
    for i in range(m):
        if b[i]==max2:
            print(i+1)
            break