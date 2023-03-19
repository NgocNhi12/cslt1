a=d=0
while True:
    n=int(input())
    if n>0:
       d=d+1
       continue
    if n<0:
        a=a+1
        continue
    else:
        print(a,'so am')
        print(d,'so duong')
        break