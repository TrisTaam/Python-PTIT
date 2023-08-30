def Try(i,j,a):
    for z in reversed(range(1,i+1)):
        a.append(z)
        j-=z
        if j==0:
            b.append(a.copy())
        elif j>0:
            Try(z,j,a)
        a.pop()
        j+=z

t=int(input())
while t>0:
    n=int(input())
    b=[]
    Try(n,n,[])
    print(len(b))
    for i in b:
        print(f"({i[0]}",end="")
        for j in range(1,len(i)):
            print(f" {i[j]}",end="")
        print(")",end=" ")
    print()
    t-=1