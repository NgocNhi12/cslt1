print("Nhap day so:")
def LaSoNguyenTo(x):
    count=0
    for i in range(1,x+1):
        if x%i==0:
            count=count+1
    if count==2:
        return True
    return False
def SoHopLe(x):
    if x<=1:
        return True
    else:
        return False
def NhapVaDem():
    j=0
    while True:
        x=int(input())
        if SoHopLe(x):
            break
        if LaSoNguyenTo(x):
            j=j+1
    return j
def InKQ(kq):
    print("Co",kq,"so nguyen to")
kq=NhapVaDem()
InKQ(kq)
    
    
