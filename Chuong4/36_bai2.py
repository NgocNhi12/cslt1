def nhap():
    n=int(input('n='))
    return n
def inkq(n):
    while True:
        for i in range(2,n+1,2):
            if i%2==0:
                print(i,end=' ')
        print()
        tt=input('Tiep tuc khong?')
        if tt=='K'or tt=='k':
            break
        n=int(input('n='))
n=nhap() 
inkq(n)     