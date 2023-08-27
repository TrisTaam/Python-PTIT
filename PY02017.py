t=int(input())
while t>0:
    n=int(input())
    a=[int(i) for i in input().split()]
    b={}
    for i in a:
        if i in b:
            b[i]+=1
        else:
            b[i]=1
    for i in b:
        if b[i]%2==1:
            print(i)
            break
    t-=1