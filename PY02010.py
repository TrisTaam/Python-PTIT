import sys

while True:
    n=int(sys.stdin.readline())
    if n==0:
        break
    a=[]
    for i in range(n):
        a.append(int(sys.stdin.readline()))
    b=min(a)
    c=max(a)
    if b==c:
        print("BANG NHAU")
    else:
        print(b,c)