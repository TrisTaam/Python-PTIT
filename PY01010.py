t=int(input())
while t>0:
    s=input()
    print(f"YES" if s[:2]==s[-2:] else "NO")
    t-=1