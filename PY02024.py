def res(n):
    s=str(n)
    p=1
    for i in s:
        p*=int(i)
    return (p,n)

t=int(input())
while t>0:
    n=int(input())
    a=[int(i) for i in input().split()]
    a.sort(key=lambda x:res(x))
    for i in a:
        print(i,end=" ")
    print()
    t-=1
