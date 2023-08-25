def res(a,b):
    if a=="Xe_con":
        if b==5:
            return 10000
        return 15000
    if a=="Xe_tai":
        return 20000
    if a=="Xe_khach":
        if b==29:
            return 50000
        return 70000

n=int(input())
a={}
for i in range(n):
    s=input().split()
    if s[3]=="IN":
        if s[4] in a:
            a[s[4]]+=res(s[1],int(s[2]))
        else:
            a[s[4]]=res(s[1],int(s[2]))
for i,j in a.items():
    print(f"{i}: {j}")