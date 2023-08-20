t=int(input())
while t>0:
    n=int(input())
    a={}
    for i in range(n):
        x=int(input())
        if x in a:
            a[x]+=1
        else:
            a[x]=1
    cnt=0
    for i in a.items():
        cnt=max(cnt,i[1])
    ans=1001
    for i in a.items():
        if i[1]==cnt:
            ans=min(ans,i[0])
    print(ans)
    t-=1