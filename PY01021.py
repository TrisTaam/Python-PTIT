t=int(input())
while t>0:
    s=input()
    s1=""
    cnt=0
    for x in s:
        if x>='0' and x<='9':
            cnt+=int(x)
        else:
            s1+=x;
    s1=''.join(sorted(s1))
    s1+=str(cnt)
    print(s1)
    t-=1