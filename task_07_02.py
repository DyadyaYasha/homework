import random
import string

def password_generator(xxx):
    znaki = (string.ascii_letters + string.digits + string.punctuation)
    #znaki = (string.ascii_letters + string.digits)
    cikla = (random.choice(znaki) for i in range(xxx))
    return ''.join(cikla)
