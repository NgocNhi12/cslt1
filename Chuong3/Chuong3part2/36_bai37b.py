while True:
    n=int(input(""))
    S=1
    j=1
    if n>=0:
        for i in range(1,n):
            S=S*i
            j=S*n
            print(j,sep="")
    else:
            break
    
        
    
