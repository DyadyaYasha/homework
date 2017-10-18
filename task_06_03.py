from collections import namedtuple

def return_namedtuple(*vipustit_crakena):
    def decorator(func):
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            if isinstance(res, tuple):
                ntp = namedtuple('ntp', vipustit_crakena)
                return ntp(*res)
            return result
        return wrapper
    return decorator





if __name__ == '__main__':

    @return_namedtuple('one', 'two', 'tri', 'chetire', 'pyat')
    def my_func():
        return 1, 2, 3, 4, 5

    print(my_func())
