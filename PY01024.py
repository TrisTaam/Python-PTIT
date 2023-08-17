def res(s):
    ans=0
    for i in range(len(s)-1):
        ans+=(ord(s[i])-48)
        if (abs(ord(s[i])-ord(s[i+1]))!=2):
            return False
    ans+=(ord(s[-1])-48)
    return ans%10==0

t=int(input())
while t>0:
    s=input()
    print(f"YES" if res(s)==True else "NO")
    t-=1