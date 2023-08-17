def reverse(n):
    return int(str(n)[::-1])

t=int(input())
while t>0:
    n=int(input())
    cnt=0
    while n%7!=0 and cnt<=1000:
        n+=reverse(n)
        cnt+=1
    print(f"{n}" if cnt<=100 else "-1")
    t-=1