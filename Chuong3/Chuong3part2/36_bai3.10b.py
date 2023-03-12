n=int(input("n="))
for i in range(1,n+1):
    if n>=1:
        if i%5!=0:
            print(i,end=" ")
        if i%5==0:
            print(i)
        
