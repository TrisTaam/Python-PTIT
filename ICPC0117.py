import sys

n=int(sys.stdin.readline())
a=set()
for i in range(n):
    s=sys.stdin.readline()
    a.add(s)
print(len(a))