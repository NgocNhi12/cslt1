
while True:
    n=int(input())
    if n>=0:
        j=1
        while n>0:
            j=j*n
            n=n-1
        print(j)
    else:
        break