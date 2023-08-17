def res(n):
    s=str(n)
    if len(s)%2==1:
        return False
    for i in s:
        if (ord(i)-48)%2==1:
            return False
    return s==s[::-1]

a=[]
for i in range(22,1000000):
    if res(i):
        a.append(i);
t=int(input())
while t>0:
    n=int(input())
    for i in a:
        if i<n:
            print(i,end=" ")
        else:
            break
    print()
    t-=1