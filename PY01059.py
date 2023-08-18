t=int(input())
while t>0:
    s=input()
    ans1=0
    ans2=1
    kt=False
    for i in range(len(s)):
        if i%2==0:
            ans1+=int(s[i])
        else:
            if s[i]!='0':
                ans2*=int(s[i])
                kt=True
    if kt==False:
        ans2=0
    print(ans1,ans2)
    t-=1