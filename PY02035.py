s=input()
k=int(input())
if len(s)%2==1:
    s=s[:-1]
a={}
for i in range(0,len(s),2):
    if s[i:i+2] in a:
        a[s[i:i+2]]+=1
    else:
        a[s[i:i+2]]=1
b=[]
for i,j in a.items():
    if (j>=k):
        b.append((i,j))
if len(b)==0:
    print("NOT FOUND")
else:
    b.sort()
    for i,j in b:
        print(i,j)