s=input()
if len(s)%2==1:
    s=s[:-1]
a=set()
for i in range(0,len(s),2):
    a.add(s[i:i+2])
b=sorted(list(a))
for i in b:
    print(i,end=" ")