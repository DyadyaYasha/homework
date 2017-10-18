from platform import system

def run_on_linux(vipustit_crakena):
    def wrapper():
        vipustit_crakena() if system() == 'Linux' else None
    return wrapper

def run_on_windows(vipustit_crakena):
    def wrapper():
        vipustit_crakena() if system() == 'Windows' else None
    return wrapper

def run_on_macos(vipustit_crakena):
    def wrapper():
        vipustit_crakena() if system() == 'MacOS' else None
    return wrapper
