def res(s,cnt):
    if len(s)==1:
        return cnt
    return res(str(sum(ord(i)-48 for i in s)),cnt+1)

s=input()
print(res(s,0))