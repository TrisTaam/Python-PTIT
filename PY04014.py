from decimal import *

class ThiSinh:
    ID=0
    COEFFICIENT=[2,2,1,1,1,1,1,1,1,1]

    def __init__(self,name,mark):
        self.name=name
        self.mark=mark
        ThiSinh.ID+=1
        self.id=f"HS{ThiSinh.ID:02}"
        s=0
        for i in range(len(self.mark)):
            s+=self.mark[i]*ThiSinh.COEFFICIENT[i]
        s/=sum(ThiSinh.COEFFICIENT)
        if s>=9:
            self.rank="XUAT SAC"
        elif s>=8:
            self.rank="GIOI"
        elif s>=7:
            self.rank="KHA"
        elif s>=5:
            self.rank="TB"
        else:
            self.rank="YEU"
        self.average=s.quantize(Decimal('0.1'),ROUND_HALF_UP)
    
    def __str__(self):
        return f"{self.id} {self.name} {self.average} {self.rank}"
    
    def __lt__(self,o):
        if self.average!=o.average:
            return self.average>o.average
        return self.id<o.id

n=int(input())
a=[]
for i in range(n):
    a.append(ThiSinh(input(),[Decimal(x) for x in input().split()]))
a.sort()
for i in a:
    print(i)