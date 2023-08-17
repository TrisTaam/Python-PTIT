def recur(n,a,b,c):
    if n==1:
        print(f"{a} -> {c}")
        return
    recur(n-1,a,c,b)
    recur(1,a,b,c)
    recur(n-1,b,a,c)

n=int(input())
recur(n,'A','B','C')