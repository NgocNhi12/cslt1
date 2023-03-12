while True:
    n=int(input(""))
    if n>=0:
        j=1
        for i in range(1,n+1,n-1):
            j=j*n
        print(j)
    else:
        break
    