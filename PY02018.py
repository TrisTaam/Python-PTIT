n=int(input())
a=[int(x) for x in input().split()]
b={}
maxa=0
for i in a:
    maxa=max(maxa,i)
    if i in b:
        b[i]+=1
    else:
        b[i]=1
for i in range(1,maxa+2):
    if i not in b:
        print(i)
        break