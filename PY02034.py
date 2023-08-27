s=input()
if len(s)%2==1:
    s=s[:-1]
a={}
for i in range(0,len(s),2):
    if s[i:i+2] in a:
        a[s[i:i+2]]+=1
    else:
        a[s[i:i+2]]=1
for i,j in a.items():
    print(i,j)