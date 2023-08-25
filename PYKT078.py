t=int(input())
while t>0:
    n,m=map(int,input().split())
    a=[int(i) for i in input().split()]
    maxa=max(a)
    for i in range(n):
        if a[i]==maxa:
            a.insert(i,m)
            break
    for i in a:
        if i<0:
            print(i,end=" ")
    for i in a:
        if i>=0:
            print(i,end=" ")
    print()
    t-=1