from math import sqrt

class Point:
    def __init__(self,x:float,y:float):
        self.x=x
        self.y=y
    
    def distance(self,o):
        return sqrt((self.x-o.x)**2+(self.y-o.y)**2)
    
class Triangle:
    def __init__(self,p1:Point,p2:Point,p3:Point):
        self.a=p1.distance(p2)
        self.b=p2.distance(p3)
        self.c=p3.distance(p1)

    def perimeter(self):
        if self.a+self.b>self.c and self.b+self.c>self.a and self.c+self.a>self.b:
            return f"{self.a+self.b+self.c:.3f}"
        else:
            return "INVALID"

a=[]
t=int(input())
for x in range(t):
    a+=[float(i) for i in input().split()]
i=0
for _ in range(t):
    b=Triangle(Point(a[i],a[i+1]),Point(a[i+2],a[i+3]),Point(a[i+4],a[i+5]))
    print(b.perimeter())
    i+=6