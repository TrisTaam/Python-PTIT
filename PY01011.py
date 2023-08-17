def res(n):
    cnt=0
    n1=n
    n2=0
    while(n1>0):
        a=n1%10
        if a%2==1:
            return False
        n2=n2*10+a
        cnt+=1
        n1//=10
    return (cnt%2==0) and (n2==n)

t=int(input())
while t>0:
    n=int(input())
    for i in range(1,n):
        if res(i):
            print(i,end=" ")
    print()
    t-=1