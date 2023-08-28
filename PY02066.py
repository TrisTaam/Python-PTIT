n=int(input())
a=[]
maxa=-10**9
while True:
    b=[int(i) for i in input().split()]
    maxa=max(maxa,max(b))
    a+=b
    if (len(a)==n):
        break
b=[]
for i in range(1,maxa+1):
    if i not in a:
        b.append(i)
if len(b)==0:
    print("Excellent!")
else:
    for i in b:
        print(i)