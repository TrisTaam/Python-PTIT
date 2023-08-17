from math import gcd

l,r=map(int,input().split())
for i in range(l,r-1):
    for j in range(i+1,r):
        if gcd(i,j)==1:
            for z in range(j+1,r+1):
                if gcd(j,z)==1 and gcd(i,z)==1:
                    print(f"({i}, {j}, {z})")