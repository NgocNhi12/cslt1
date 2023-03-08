n=int(input("n="))
j=0
if n==2:
    print(n,"la SNT")
else:
    if n%2==0:
        print(n,"khong la SNT")
    else:
        for i in range(1,n+1):
            if n%i==0:
                j=j+1
        if j==2:
            print(n,"la SNT")
        else:
            print(n,"khong la SNT")