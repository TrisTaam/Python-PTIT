n=int(input())
a=[float(x) for x in input().split()]
maxa=max(a)
mina=min(a)
s=sum(a)
for i in a:
    if i==maxa or i==mina:
        s-=i
        n-=1
print(f"{s/n:.2f}")