def res(s):
    if len(s)%2==0:
        return False
    if s[0]==s[1]:
        return False
    for i in range(2,len(s),2):
        if s[i]!=s[i-2]:
            return False
    return True

t=int(input())
while t>0:
    s=input()
    print("YES" if res(s) else "NO")
    t-=1