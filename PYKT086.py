with open("DATA.in") as inp:
    t=int(inp.readline())
    while t>0:
        k=int(inp.readline())
        n=int(inp.readline(),2)
        s=""
        while n>0:
            i=n%k
            if (i<10):
                s=str(i)+s
            else:
                s=chr(i-10+ord('A'))+s
            n//=k
        print(s)
        t-=1