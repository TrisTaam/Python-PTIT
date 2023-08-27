n,m=map(int,input().split())
a=sorted(list(set([int(i) for i in input().split()])))
b=sorted(list(set([int(i) for i in input().split()])))
print("YES" if a==b else "NO")