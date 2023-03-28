month=int(input("\nNhap vao thang tu 1 den 12: "))
day=int(input("Nhap vao ngay tu 1 den 31: "))
year=str(int(input("Nhap vao nam: ")))
def kidieu():
    a=int(year[2:5])
    kq=str(day)+'/'+str(month)+'/'+year
    if ((month*day)!=a):
        print(kq,"is not magic")
    else:
        print(kq,"is magic")
def kq():
    print(kq)
k=kidieu()