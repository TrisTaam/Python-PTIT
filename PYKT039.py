def res(a,b):
    for i in range(len(a)):
        if a[i]>b[i]:
            return False
    return True

t=int(input())
while t>0:
    n=int(input())
    a=sorted([int(i) for i in input().split()])
    b=sorted([int(i) for i in input().split()])
    print("YES" if res(a,b) else "NO")
    t-=1