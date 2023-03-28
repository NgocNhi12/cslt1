import random
kitu = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
number = '0123456789'
chucai = ''
num = ''
for i in range(3):
    chucai =chucai +  random.choice(kitu)
for i in range(4):
    num =num + random.choice(number)
print('Bien so cua ban la', num, chucai)

 