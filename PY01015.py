def res(s):
    return s=="".join(sorted(s))

t=int(input())
while t>0:
    s=input()
    print(f"YES" if res(s) else "NO")
    t-=1