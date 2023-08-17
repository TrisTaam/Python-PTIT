s=input()
cnt=0
for i in s:
    if (i>='A') and (i<='Z'):
        cnt+=1
s=s.lower() if (cnt<=len(s)-cnt) else s.upper()
print(s)