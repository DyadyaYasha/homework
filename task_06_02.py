from time import sleep

def pause(vipustit_crakena):
    def decorator(func):
        def wrapper(*args, **kwargs):
            sleep(vipustit_crakena)
            return func(*args, **kwargs)
        return wrapper
    return decorator
