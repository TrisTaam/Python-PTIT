from math import gcd

t=int(input())
while t>0:
    s1=input()
    s2=s1[::-1]
    print(f"YES" if gcd(int(s1),int(s2))==1 else "NO")
    t-=1