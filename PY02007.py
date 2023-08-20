a=list()
while True:
    try:
        tmp=map(int,input().split())
        for i in tmp:
            a.append(i)
    except:
        break;
b=set()
for i in a:
    b.add(i%42)
print(len(b))