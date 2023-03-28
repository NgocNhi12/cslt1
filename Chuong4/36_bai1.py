def nhap():
    n=int(input('n='))
    return n
def giaithua(n):
    j=1
    for i in range(1,n+1):
        j=j*i
    return(j)
def inkq(n,X):
    print(n,'!=',X,sep='') 
n=nhap()
X=giaithua(n) 
inkq(n,X)  