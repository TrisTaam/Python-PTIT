def res(n):
    if n<=2:
        return 1.0
    if n<=4:
        return 2.5
    if n<=6:
        return 3.0
    if n<=9:
        return 3.5
    if n<=12:
        return 4.0
    if n<=15:
        return 4.5
    if n<=19:
        return 5.0
    if n<=22:
        return 5.5
    if n<=26:
        return 6.0
    if n<=29:
        return 6.5
    if n<=32:
        return 7.0
    if n<=34:
        return 7.5
    if n<=36:
        return 8.0
    if n<=38:
        return 8.5
    return 9.0

t=int(input())
while t>0:
    s=input().split()
    mark=(res(int(s[0]))+res(int(s[1]))+float(s[2])+float(s[3]))/4
    tmp=mark-int(mark)
    if tmp>=0.75:
        mark=int(mark)+1.0
    elif tmp>=0.25:
        mark=int(mark)+0.5
    else:
        mark=int(mark)
    print(f"{mark:.1f}")
    t-=1