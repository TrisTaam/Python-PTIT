def res(n):
    return n*(n-1)//2

n=int(input())
a=[]
for i in range(n):
    a.append(input())
ans=0
for i in range(n):
    cnt=0
    for j in range(n):
        if a[i][j]=='C':
            cnt+=1
    ans+=res(cnt)
for i in range(n):
    cnt=0
    for j in range(n):
        if a[j][i]=='C':
            cnt+=1
    ans+=res(cnt)
print(ans)