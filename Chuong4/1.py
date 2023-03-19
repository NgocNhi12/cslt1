from random  import randint
print("nhap bua,bao,keo:")
n=int(input())
while n!=0:
    m=int(input())
    if m!=0:
        player = int(input())
        computer =randint(1,3)
        if computer=="bua":
            computer=1
        if computer=="bao":
            computer=2
        if computer=="keo":
            computer=3
        print("---")
        print("you choose: " , player )
        print("computer chooses: " ,computer )
        print("---")
        if player==computer:
            print("draw")
        else:
            if player ==3:
                if computer==1:
                    print("lose")
                else:
                    print("win")
            elif player ==1:
                if computer==3:
                    print("win")
                else:
                    print("lose")
            elif player ==2:
                if computer==3:
                    print("lose")
                else:
                    print("win")
            else:
                print("nhap lai, nhap sai")


