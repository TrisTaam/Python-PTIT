def res(a,b):
    if b==1:
        if a<=19:
            return "Ma Ket"
        else:
            return "Bao Binh"
    if b==2:
        if a<=18:
            return "Bao Binh"
        else:
            return "Song Ngu"
    if b==3:
        if a<=20:
            return "Song Ngu"
        else:
            return "Bach Duong"
    if b==4:
        if a<=19:
            return "Bach Duong"
        else:
            return "Kim Nguu"
    if b==5:
        if a<=20:
            return "Kim Nguu"
        else:
            return "Song Tu"
    if b==6:
        if a<=20:
            return "Song Tu"
        else:
            return "Cu Giai"
    if b==7:
        if a<=22:
            return "Cu Giai"
        else:
            return "Su Tu"
    if b==8:
        if a<=22:
            return "Su Tu"
        else:
            return "Xu Nu"
    if b==9:
        if a<=22:
            return "Xu Nu"
        else:
            return "Thien Binh"
    if b==10:
        if a<=22:
            return "Thien Binh"
        else:
            return "Thien Yet"
    if b==11:
        if a<=22:
            return "Thien Yet"
        else:
            return "Nhan Ma"
    if b==12:
        if a<=21:
            return "Nhan Ma"
        else:
            return "Ma Ket"

t=int(input())
while t>0:
    a,b=map(int,input().split())
    print(res(a,b))
    t-=1