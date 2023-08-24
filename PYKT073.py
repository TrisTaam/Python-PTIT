n=int(input())
a=[]
for i in range(n):
    a.append(len(input().split()))
i=0
b=[]
while i<len(a):
    if a[i]==6:
        b.append(1)
        while i<len(a) and (a[i]==6 or a[i]==8):
            i+=1
    elif a[i]==7:
        b.append(2)
        i+=4
    else:
        i+=1
print(len(b))
for i in b:
    print(i)