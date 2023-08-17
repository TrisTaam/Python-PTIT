def res(s):
    return (len(s)>1) and (s==s[::-1])

t=int(input())
while t>0:
    s=input()
    s1=str(sum(int(i) for i in s))
    print("YES" if res(s1) else "NO")
    t-=1