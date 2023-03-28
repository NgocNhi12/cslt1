n=int(input())
s=''
for i in range(1,n+1):
    for j in range(1,n+1):
        a=n%10
        if a==1:
            s='one'+s
        elif a==2:
            s='two'+s
        elif a==3:
            s='three'+s
        elif a==4:
            s='four'+s
        elif a==5:
            s='five'+s
        elif a==6:
            s='six'+s
        elif a==7:
            s='seven'+s
        elif a==8:
            s='eight'+s
        elif a==9:
            s='nine'+s
        n=n//10
        if n==0:
            break
        else:
            continue
        print(j)

