a=[0]*93
a[1]=a[2]=1
for i in range(3,93):
    a[i]=a[i-1]+a[i-2]
t=int(input())
while t>0:
    l,r=map(int,input().split())
    for i in range(l,r+1):
        print(a[i],end=" ")
    print()
    t-=1