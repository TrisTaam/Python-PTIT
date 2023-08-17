t=int(input())
while t>0:
    n=int(input())
    a=1 if n%2==1 else 2
    s=0
    for i in range(a,n+1,2):
        s+=1/i
    print(f"{s:.6f}")
    t-=1