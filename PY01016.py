t=int(input())
while t>0:
    s=input()
    for i in range(0,len(s),2):
        print(s[i]*int(s[i+1]),end="")
    print()
    t-=1