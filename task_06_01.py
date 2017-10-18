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


@run_on_macos
def my_func():
    print('Функция выполняется только на MacOS!')

@run_on_windows
def my_func():
    print('Функция выполняется только на Windows!')

@run_on_linux
def my_func():
    print('Функция выполняется только на Linux!')
