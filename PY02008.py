from math import sqrt

def nto(n):
    end=int(sqrt(n))
    for i in range(2,end+1):
        if n%i==0:
            return False
    return n>1

n,x=map(int,input().split())
print(x,end=" ")
i=2
while n>0:
    while nto(i)==False:
        i+=1
    n-=1
    x+=i
    i+=1
    print(x,end=" ")