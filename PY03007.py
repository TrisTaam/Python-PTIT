a=[]
while True:
    try:
        for i in input().split():
            a.append(i.lower())
    except:
        break
kt=True
for i in a:
    if kt:
        i=i.capitalize()
    if i[-1]=='.' or i[-1]=='?' or i[-1]=='!':
        kt=True
        print(i[:-1])
    else:
        kt=False
        print(i,end=" ")