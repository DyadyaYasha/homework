def is_palindrome(s):
    def vfun(sh): 
        sh = str(sh)
        sh = sh.lower()
        L = list(' !@#%^&*();:?,.\/|')
        for i in L:
            sh = sh.replace(i, '')
        spi = list(sh)
        spi.reverse()
        sk = ''.join(spi)
        return False if sh != sk else True
    return vfun