def res(a,x):
    for i in a:
        if i//x==i//(x+1):
            return False
    return True

n=int(input())
a=[int(i) for i in input().split()]
mina=min(a)
ans=0
for i in reversed(range(1,mina+1)):
    if res(a,i):
        for j in a:
            ans+=(j//(i+1)+1)
        break
print(ans)