def count(s):
    a={}
    for i in s:
        if i in a:
            a[i]+=1
        else:
            a[i]=1
    return a

t=int(input())
for i in range(1,t+1):
    print(f"Test {i}:",end=" ")
    s1=input()
    s2=input()
    a=count(s1)
    b=count(s2)
    kt=True
    for i in a:
        if (i not in b) or (b[i]!=a[i]):
            kt=False
            break
    print("YES" if kt else "NO")