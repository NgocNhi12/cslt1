a=float(input("a="))
b=float(input("b="))
c=float(input("c="))
max=c
min=a
if max<b:
    max=b
    min=a
    print("So lon nhat la:", max)
    print("So be nhat la:", min)
if max<a:
    max=a
    min=b
    print("So lon nhat la:", max)
    print("So be nhat la:", min)