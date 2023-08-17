p="ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while True:
    inp=input().split()
    if (len(inp)==1):
        break
    k=int(inp[0])
    s=inp[1]
    s1=""
    for i in s:
        s1=p[(p.index(i)+k)%28]+s1
    print(s1)