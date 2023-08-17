def res(s):
    for i in s:
        if (i!='4') and (i!='7'):
            return False
    return True

t=int(input())
while t>0:
    s=input()
    print(f"YES" if res(s)==True else "NO")
    t-=1