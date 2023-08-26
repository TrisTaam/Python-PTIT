s1=input().lower().split()
s2=input().lower().split()
a=set()
b=set()
for i in s1:
    a.add(i)
    b.add(i)
c=set()
for i in s2:
    a.add(i)
    c.add(i)
a=sorted(a)
for i in a:
    print(i,end=" ")
print()
b=sorted(b)
c=sorted(c)
for i in b:
    if i in c:
        print(i,end=" ")