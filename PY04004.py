from math import gcd

class PhanSo:
    def __init__(self,tu,mau):
        tmp=gcd(tu,mau)
        self.tu=tu//tmp
        self.mau=mau//tmp

    def add(self,o):
        a=self.tu*o.mau+self.mau*o.tu
        b=self.mau*o.mau
        return PhanSo(a,b)
        
    def __str__(self):
        return f"{self.tu}/{self.mau}"
    
a,b,c,d=map(int,input().split())
e=PhanSo(a,b)
f=PhanSo(c,d)
print(e.add(f))