t=int(input())
while t>0:
    s=input().split()
    ans=""
    for i in s:
        if (len(ans+i)>100):
            break
        ans+=(i+" ")
    print(ans)
    t-=1