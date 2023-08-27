t=int(input())
while t>0:
    n,m,k=map(int,input().split())
    a=[int(i) for i in input().split()]
    b=[int(i) for i in input().split()]
    c=[int(i) for i in input().split()]
    i=0
    j=0
    z=0
    d=[]
    while i<n and j<m and z<k:
        if a[i]==b[j] and b[j]==c[z]:
            d.append(a[i])
            i+=1
            j+=1
            z+=1
        elif a[i]<b[j]:
            i+=1
        elif b[j]<c[z]:
            j+=1
        else:
            z+=1
    if len(d)==0:
        print("NO")
    else:
        for i in d:
            print(i,end=" ")
        print()
    t-=1