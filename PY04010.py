class ThiSinh:
    def __init__(self,name,dob,mark):
        self.name=name
        self.dob=dob
        self.mark=mark
    
    def getSum(self):
        return sum(self.mark)
    
    def __str__(self):
        return f"{self.name} {self.dob} {self.getSum():.1f}"
    
name=input()
dob=input()
mark=[]
for i in range(3):
    mark.append(float(input()))
a=ThiSinh(name,dob,mark)
print(a)