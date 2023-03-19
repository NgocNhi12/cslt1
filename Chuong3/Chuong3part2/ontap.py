n=int(input('Nhap n(1<=n<=90:)'))
if n<=0 or n>=90:
    print("Nhap sai, yeu cau nhap lai")
else:
    for i in range(1,n+1):
        print('*'*i)
    
    