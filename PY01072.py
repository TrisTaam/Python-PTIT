from itertools import combinations

n,k=map(int,input().split())
a=list(set(map(int,input().split())))
b=list(combinations(sorted(a),k))
for i in b:
    for j in i:
        print(j,end=" ")
    print()