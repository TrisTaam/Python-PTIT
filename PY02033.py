s=input()
if len(s)%2==1:
    s=s[:-1]
a=[]
for i in range(0,len(s),2):
    if s[i:i+2] not in a:
        a.append(s[i:i+2])
for i in a:
    print(i,end=" ")