def res(s,a,b):
    return int(s.replace(a,b))

t=int(input())
while t>0:
    a,b=input().split()
    s1=input().split()
    if (len(s1)==2):
        s2=s1[1]
    else:
        s2=input()
    s1=s1[0]
    ans1=res(s1,a,b)+res(s2,a,b)
    ans2=res(s1,b,a)+res(s2,b,a)
    print(min(ans1,ans2),max(ans1,ans2))
    t-=1