from queue import Queue

def res(n):
    s=str(n)
    a=s.count('2')
    return a*2>len(s)

a=[]
q=Queue()
q.put(1)
q.put(2)
a=[]
while True:
    b=q.get()
    if res(b):
        a.append(b)
        if (len(a)==1000):
            break
    for i in range(3):
        q.put(b*10+i)
a.sort()

t=int(input())
while t>0:
    n=int(input())
    for i in range(n):
        print(a[i],end=" ")
    print()
    t-=1