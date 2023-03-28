from random import randint
import random
def randomPassword():
    I=randint(7,10)
    password=""
    for i in range(I):
        password=password+chr(randint(33,126))
    return password
rPassword=randomPassword()
print("Mat khau ngau nhien cua ban la:",rPassword)
 