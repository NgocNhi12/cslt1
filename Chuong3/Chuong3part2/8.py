while True:
    S=1
    n=int(input())
    if n>=0:
        j=1
        for i in range(1,n):
            S=S*i
            j=S*n
        print(j)
    else:
        break
            