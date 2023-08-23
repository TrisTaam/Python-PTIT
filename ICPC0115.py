a=[1]
for i in range(1,10):
    a.append(a[i-1]*i) 
t=int(input())
while t>0:
    n=input()
    s=sum(a[int(i)] for i in n)
    print("Yes" if int(n)==int(s) else "No")
    t-=1