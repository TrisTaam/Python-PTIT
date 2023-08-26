n=int(input())
a=[int(i) for i in input().split()]
ans=10**9
z=-1
for i in range(n):
    cnt=0
    for j in range(n):
        cnt+=abs(a[i]-a[j])
    if ans>cnt:
        ans=cnt
        z=a[i]
print(ans,z)