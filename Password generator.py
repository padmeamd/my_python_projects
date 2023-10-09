import random
import time 

a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
b = 'abcdefghijklmnopqrstuvwxyz'
c = '0123456789'
d = '!@%&{}[]~/$?_=-*|".,'

all = a + b + c + d
length = 8
password = "".join(random.sample(all,length))
print("Generating your password...")
time.sleep(3)
print("Your password is:")
time.sleep(1.5)
print(password)
input()
