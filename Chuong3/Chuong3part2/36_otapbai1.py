n=int(input("n="))
if n==0:
    print(n,"!=",1,sep="")
else:
    j=1
    for i in range(1,n+1,1):
        j=j*i
    print(n,"!=",j,sep="")
    