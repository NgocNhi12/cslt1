def Nhap():
    n=int(input('Nhap so nguyen n'))
    return n
def Tinh(n):
    S=0
    for x in range(1,n+1):
        S=S+x
    return S
def InKQ(n,S):
    print('Tong cua ',n,' so nguyen duong dau tien=',S,sep='')

InKQ(9,S)