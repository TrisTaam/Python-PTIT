n=int(input())
a=[]
for i in range(n):
    a.append([int(j) for j in input().split()])
s=sum(sum(i) for i in a)//((n-1)*2)
for i in a:
    print((sum(i)-s)//(n-2),end=" ")