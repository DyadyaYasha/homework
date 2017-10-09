def dec2bin(number):

    n = ''

    while number > 0:
        y = str(number % 2)
        n = y + n
        number = int(number // 2)
    return n

def dec2oct(number):

    n = ''

    while number > 0:
        y = str(number % 8)
        n = y + n
        number = int(number // 8)
    return n

def dec2hex(number):

    d = {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9',10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}

    n = ''

    while number != 0:
        y = number % 16
        number = number // 16
        n += d[y]

    n = ''.join(reversed(n))

    return n

def bin2dec(number):

    y = 0

    n = len(number)

    for i in number:
        y += int(i) * 2 ** (n - 1)

        n -= 1
    return y

def oct2dec(number):

    y = 0

    n = len(number)

    for i in number:
        y += int(i) * 8 ** (n - 1)

        n -= 1
    return y

def hex2dec(number):
    
    y = 0

    n = len(number)
    
    d = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9,'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
    
    for i in number:
        for nom in d:
            if i == nom:
                y += d[nom]*(16**(n-1))
                   
        n -= 1
        
    return y

