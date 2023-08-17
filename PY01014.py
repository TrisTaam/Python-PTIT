a,k,n=map(int,input().split())
start=k-a%k
if a+start>n:
    print(-1)
else:
    for i in range(start,n-a+1,k):
        print(i,end=" ")