n=int(input())
a=[]
for i in range(n):
    b=[int(i) for i in input().split()]
    a.append(b)
k=int(input())
s=0
for i in range(n):
    for j in range(n):
        if i<j:
            s+=a[i][j]
        elif i>j:
            s-=a[i][j]
s=abs(s)
print("YES" if s<=k else "NO")
print(s)