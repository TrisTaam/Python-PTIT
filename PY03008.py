n=int(input())
a=[]
for i in range(n):
    a.append([]*n)
for i in range(n-1):
    x,y=map(int,input().split())
    a[x-1].append(y-1)
    a[y-1].append(x-1)
kt=False
for i in a:
    if len(i)==n-1:
        kt=True
        break
print("Yes" if kt else "No")