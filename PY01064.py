t=int(input())
while t>0:
    n,k=map(int,input().split())
    cnt=0
    while k%2==0:
        k/=2
        cnt+=1
    print(chr(65+cnt))
    t-=1