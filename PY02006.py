def res(a:list,b:list):
    for i in range(len(a)):
        if a[i]>b[i]:
            return False
    return True

t=int(input())
while t>0:
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    b=list(map(int,input().split()))
    b.sort()
    print("YES" if res(a,b) else "NO")
    t-=1