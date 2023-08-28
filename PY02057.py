from math import sqrt

n,m=map(int,input().split())
a=[]
maxa=-10**9
mina=10**9
for i in range(n):
    b=[int(i) for i in input().split()]
    for i in b:
        maxa=max(maxa,i)
        mina=min(mina,i)
    a.append(b)
ans=-10**9
tmp=maxa-mina
for i in a:
    for j in i:
        if j==tmp:
            ans=max(ans,j)
if ans==-10**9:
    print("NOT FOUND")
else:
    print(ans)
    for i in range(n):
        for j in range(m):
            if a[i][j]==ans:
                print(f"Vi tri [{i}][{j}]")