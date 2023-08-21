n=int(input())
a=[int(i) for i in input().split()]
s=[]
for i in a:
    if len(s)==0:
        s.append(i)
    elif (s[-1]+i)%2==0:
        s.pop()
    else:
        s.append(i)
print(len(s))