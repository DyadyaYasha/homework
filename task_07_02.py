import random

def password_generator(n):
    sp = ('@#$%&*')
    sp = list(sp)
    sp2 = [random(sp) for i in range(n)]
    yield sp
    print(sp2)

print(*password_generator(16))
