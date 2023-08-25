n=int(input())
kt=True
cnt=0
for i in range(n):
    s=input()
    if kt:
        print(s,end=": ")
        cnt=0
        kt=False
    elif s!="":
        cnt+=1
    if s=="":
        kt=True
        print(cnt)
print(cnt)