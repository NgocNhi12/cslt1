print("Nhap day so:")
def LaSoNguyenTo(x):
    if x<2:
        return False
    for i in range(2,x//2+1):
        if x%i==0:
            return False
        else:
            return True
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
