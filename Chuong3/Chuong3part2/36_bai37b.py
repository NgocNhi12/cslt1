n=int(input(""))
if n>0:
    giaithua=1
    for i in range(1,n+1):
        giaithua=giaithua*i
    print(giaithua)
elif n==0:
    print("1")
