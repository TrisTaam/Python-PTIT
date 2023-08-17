def res(s):
    if len(set(s))!=2:
        return False
    for i in range(2,len(s)):
        if s[i]!=s[i-2]:
            return False
    return True

t=int(input())
while t>0:
    s=input()
    print("YES" if res(s) else "NO")
    t-=1