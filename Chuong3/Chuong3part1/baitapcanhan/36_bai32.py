M1=int(input("M1="))
M2=int(input("M2="))
M3=int(input("M3="))
S=int(input("S="))
if S<=100:
    print("Phai tra=",S*M1)
elif S<=150:
    print("Phai tra=",100*M1+(S-100)*M2)
else:
    print("Phai tra=",100*M1+50*M2+(S-150)*M3,sep="")
   