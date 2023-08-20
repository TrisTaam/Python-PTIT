t=int(input())
while t>0:
    n=int(input())
    a=[int(x) for x in input().split()]
    b={}
    for i in a:
        if i in b:
            b[i]+=1
        else:
            b[i]=1
    cnt=0
    for i in b.items():
        cnt=max(cnt,i[1])
    if cnt<=n/2:
        print("NO")
    else:
        ans=10**6+1
        for i in b.items():
            if i[1]==cnt:
                ans=min(ans,i[0])
        print(ans)
    t-=1