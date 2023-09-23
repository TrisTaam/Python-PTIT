while True:
    try:
        a=input().lower().split()
        s=""
        for x in a:
            if x=="." or x=="!" or x=="?":
                s=s[:-1]+x
                print(s)
                s=""
            else:
                if not s:
                    x=x[0].upper()+x[1:]
                s+=(x+" ")
                if x[-1]=='.' or x[-1]=='!' or x[-1]=='?':
                    print(s)
                    s=""
        if s:
            print(s[:-1]+".")
    except:
        break