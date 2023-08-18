def res(s):
    ans=1
    for i in s:
        if i!='0':
            ans*=int(i)
    return ans

t=int(input())
while t>0:
    s=input()
    print(res(s))
    t-=1