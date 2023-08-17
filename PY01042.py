def res(s):
    for i in s:
        if (i>'3'):
            return False
    return True

t=int(input())
while t>0:
    s=input()
    print("YES" if res(s) else "NO")
    t-=1