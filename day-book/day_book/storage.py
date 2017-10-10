import os.path as Path
import sqlite3

SQL_SELECT_ALL = """
    SELECT id, day, month, zagolovok, zadacha, status
    FROM daybook
""" 

def menu():
    loop = True
    while loop == True:
        print(
            '\n Ежедневник. Выберите действие:\n\n'
            ' 1 - Вывести список задач\n'
            ' 2 - Добавить задачу\n'
            ' 3 - Отредактировать задачу\n'
            ' 4 - Завершить задачу\n'
            ' 5 - Начать задачу сначала\n'
            ' 0 - Выход'
        )
        vvod = input('\n Введите число: ')

        if vvod == '1':
            spizad()
        elif vvod == '2':
            print('\n Ввввжух и добавляю задачу\n')
        elif vvod == '3':
            print('\n Ввввжух и редактирую задачу\n')
        elif vvod == '4':
            print('\n Ввввжух и завершаю задачу\n')
        elif vvod == '5':
            print('\n Ввввжух и начинаю задачу сначала\n')
        elif vvod == '0':
            print('\n Ввввжух и выхожу\n')
            loop = False
        else:
            print('\n Неизвестная команда. Попробуй снова. Я знаю ты сможешь!\n')

def spizad():
    loop2 = True
    while loop2 == True:
        print(
            '\n Список задач. Выберите действие:\n\n'
            ' 1 - За день\n'
            ' 2 - За неделю\n'
            ' 3 - За месяц\n'
            ' 0 - Вернуться в главное меню'
        )
        vvod2 = input('\n Введите число: ')

        if vvod2 == '1':
            #print('\n Ввввжух и вывожу список задач за день\n')
            zaden()
        elif vvod2 == '2':
            print('\n Ввввжух и вывожу список задач за неделю\n')
        elif vvod2 == '3':
                print('\n Ввввжух и вывожу список задач за месяц\n')
        elif vvod2 == '0':
            print('\n Ввввжух и возвращаюсь в главное меню\n')
            loop2 = False
        else:
            print('\n Неизвестная команда. Попробуй снова. Я знаю ты сможешь!\n')

def zaden():
    loop3 = True
    while loop3 == True:
        print(
            '\n Список задач. За день. Выберите действие:\n\n'
            ' 1 - За сегодня\n'
            ' 2 - За конкретный день\n'
            ' 0 - Вернуться назад'
        )
        vvod3 = input('\n Введите число: ')

        if vvod3 == '1':
            print('\n Ввввжух и вывожу список задач за сегодня\n')
        elif vvod3 == '2':
            print('\n Ввввжух и вывожу список задач за конкретный день\n')
        elif vvod3 == '0':
            print('\n Ввввжух и возвращаюсь назад\n')
            loop3 = False
        else:
            print('\n Неизвестная команда. Попробуй снова. Я знаю ты сможешь!\n')


if (__name__=="__main__"):
    menu()



