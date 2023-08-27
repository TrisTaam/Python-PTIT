n=int(input())
while n>=10:
    s=str(n)
    m=len(s)
    n=int(s[:m//2])+int(s[m//2:])
    print(n)