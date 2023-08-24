def res(a):
    if len(a)!=4:
        return False
    for i in a:
        try:
            if int(i)<0 or int(i)>255:
                return False
        except:
            return False
    return True

t=int(input())
while t>0:
    a=input().split(".")
    print("YES" if res(a) else "NO")
    t-=1