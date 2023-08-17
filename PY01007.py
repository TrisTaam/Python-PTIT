from math import log,ceil

t=int(input())
while t>0:
    inp=input().split()
    n=float(inp[0])
    x=float(inp[1])
    m=float(inp[2])
    res=ceil(log(m/n)/log(1+x/100))
    print(res)
    t-=1