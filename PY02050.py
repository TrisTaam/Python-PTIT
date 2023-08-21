t=int(input())
while t>0:
    n=int(input())
    a=[int(i) for i in input().split()]
    s=[]
    for i in range(n):
        while len(s)>0 and a[i]>=a[s[-1]]:
            s.pop()
        print(i+1 if len(s)==0 else i-s[-1],end=" ")
        s.append(i)
    print()
    t-=1
