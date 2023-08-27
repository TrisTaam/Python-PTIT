def res(n):
    return (n-1)*n//2;

n=int(input())
a=[]
ans=0
for i in range(n):
    s=input()
    cnt=0
    for i in s:
        if i=='C':
            cnt+=1
    a.append(s)
    ans+=res(cnt)
for i in range(n):
    cnt=0
    for j in range(n):
        if a[j][i]=='C':
            cnt+=1
    ans+=res(cnt)
print(ans)