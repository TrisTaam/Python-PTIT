t=int(input())
while t>0:
    s=input()
    print("YES" if s[0]==s[-1] else "NO")
    t-=1