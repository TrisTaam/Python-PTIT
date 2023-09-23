class CaThi:
    ID=0
    def __init__(self,date,time,room):
        CaThi.ID+=1
        self.id=f"C{CaThi.ID:03}"
        self.date=date
        self.time=time
        self.room=room
    
    def reverseDate(s:str):
        a=s.split("/")
        return f"{a[2]}/{a[1]}/{a[0]}"
    
    def __str__(self):
        return f"{self.id} {self.date} {self.time} {self.room}"
    
    def __lt__(self,o):
        if self.date!=o.date:
            return CaThi.reverseDate(self.date)<CaThi.reverseDate(o.date)
        if self.time!=o.time:
            return self.time<o.time
        return self.id<o.id

with open("CATHI.in") as inp:
    n=int(inp.readline())
    a=[]
    for i in range(n):
        a.append(CaThi(inp.readline().strip(),inp.readline().strip(),inp.readline().strip()))
    a.sort()
    for i in a:
        print(i)