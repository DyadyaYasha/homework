def is_palindrome(s): 
    sh = str(s)
    sh = sh.lower()
    L = list(' !@#%^&*();:?,.\/|')
    for i in L:
        sh = sh.replace(i, '')
    spi = list(sh)
    spi.reverse()
    sk = ''.join(spi)
    return False if sh != sk else True

if (__name__=="__main__"):
    print(is_palindrome('Spam Aps'))
