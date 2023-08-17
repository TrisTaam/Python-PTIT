def res(s):
    if len(s)<3:
        return False
    i=0
    while (i<len(s)-1) and (s[i]<s[i+1]):
        i+=1
    for j in range(i+1,len(s)):
        if s[j]>=s[j-1]:
            return False
    return True

t=int(input())
while t>0:
    s=input()
    print("YES" if res(s) else "NO")
    t-=1