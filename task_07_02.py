import random
import string

def passgen(xxx):
    znaki = (string.ascii_letters + string.digits + string.punctuation)
    #sym = (string.ascii_letters + string.digits)
    cikla = (random.choice(znaki) for i in range(xxx))
    return ''.join(cikla)
