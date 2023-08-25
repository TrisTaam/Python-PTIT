n=int(input())
a=[]
for i in range(n):
    s=input()
    b,c=map(int,input().split())
    a.append((s,b,c))
a.sort(key=lambda x:(-x[1],x[2],x[0]))
for i in a:
    print(i[0],i[1],i[2])