def nhap():
    n=int(input())
    print("Nhap",n,"so nguyen")
    return n
def Nhapvadem(n):
    s=0
    while True:
        for i in range(1,n+1):
            n=int(input())
            if n>0:
                if n%2==0:
                    s=s+1
                    continue
        print("",end="")
        return s
    
def inkq(kq):
    print("So chu so chan la:",kq)
    
n=nhap()
kq=Nhapvadem(n)
inkq(kq)