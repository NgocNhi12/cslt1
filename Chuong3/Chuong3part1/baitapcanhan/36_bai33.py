x=float(input("x="))
y=float(input("y="))
ch=str(input("Phep toan:"))
if ch=="+":
    print(x,"+",y,"=",x+y,sep="")
elif ch=="-":
    print(x,"-",y,"=",x-y,sep='')
elif ch=="*":
    print(x,"*",y,"=",x*y,sep="")
elif ch=="/":
    if y==0:
        print("Khong hop le")
    elif y!=0:
        print(x,"/",y,"=",x/y,sep="")
else:
    print("Khong hop le")
