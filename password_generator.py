import random
H = int(input("Password long: \n"))
p = 0
while p < H:
    a = random.choice('!#$%&?@_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890')
    print(a,end='')
    p += 1
