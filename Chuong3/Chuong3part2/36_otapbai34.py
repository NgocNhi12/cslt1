while True:
    a=float(input("a="))
    b=float(input("b="))
    k=str(input("Toan tu:"))
    if k=="+":
        print(a,"+",b,"=",a+b,sep="")
    elif k=="-":
        print(a,"-",b,"=",a-b,sep='')
    elif k=="*":
        print(a,"*",b,"=",a*b,sep="")
    elif k=="/":
        if b==0:
            print("Khong hop le")
        elif b!=0:
            print(a,"/",b,"=",a/b,sep="")
tt=str(input('Tiep tuc:'))
if tt=='t' or tt=='T':
    break
     