n=int(input())
j=0
max=2
if n==2:
    print(max)
else:
    for i in range(1,n+1):
        if n%i==0:
            j=j+1
            max=max-j
            print(max)
    if j==2:
        print(max)
   