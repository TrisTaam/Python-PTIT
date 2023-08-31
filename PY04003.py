from math import gcd

class PhanSo:
    def __init__(self,tu,mau):
        tmp=gcd(tu,mau)
        self.tu=tu//tmp
        self.mau=mau//tmp
        
    def __str__(self):
        return f"{self.tu}/{self.mau}"
    
a,b=map(int,input().split())
c=PhanSo(a,b)
print(c)