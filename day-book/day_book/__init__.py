import os.path as Path
import sys

from day_book import storage

get_connection = lambda : storage.connect('daybook.sqlite')


def action_add_zad():
    """Добавить задачу"""
    zad = input('\nВведите задачу: ')

    with get_connection() as conn:
        new_zad = storage.add_zad(conn, zad)

    print('Ваша задача: "{}" добавлена в ежедневник'.format(new_zad))
    # если мы отрицаем пустоту т.е. not то возвращаем истину

    if not zad:
        return



def action_find_by_zagol():
    """Найти задачу по заголовку"""
    zagol = input('Введите заголовок задачи: ')
    # kлюбую введённую строчку можно привести к истене, пустой ввод игнорируется

    if zagol:
        with get_connection() as conn:
            row = storage.zad_by_zagol(conn, zagol)

        if row:
            zad = row.get('zadacha')
            print('Ваша задача: {}'.format(zad)) # format вставляет то что нам нужно в {}
        else:
            print('Заголовок "{}" не существует'.format(zagol))



def action_zad_all():
    """Вывести все url-адреса"""
    with get_connection() as conn:
        rows = storage.zad_all(conn)

    template = '{row[zagol]} - {row[zadacha]} - {row[day]} - {row[month]}' # если проименовать значения то можно подставить квадратные скобки в которые format вытащит из словаря нужные данные
    # дату можно еще форматироать в удобный вид
    # можно нумеровать template = '{0} - {0} - {1}' тогда format нужно передать всего 2 аргумента

    for row in rows:
        print(template.format(row=row))


def action_redact_zad():
    """Редактировать задачу"""


def action_end_zad():
    """Закончить задачу"""


def action_restart_zad():
    """Начать задачу сначала"""


def action_show_menu():
    """Показать меню"""
    print("""
 Ежедневник. Выберите действие:

 1. - Вывести список задач
 2. - Добавить задачу
 3. - Отредактировать задачу
 4. - Завершить задачу
 5. - Начать задачу сначала
 m. - Показать меню
 q. - Выйти""")


def action_exit():
    """Выйти из программы"""
    sys.exit(0)



def main():
    creation_schema = Path.join( # склеивает путь файла с разделитилем определённой OS
        Path.dirname(__file__), 'schema.sql' # позволяет вернуть родительскую директорию файла и отрежет файл оставив только путь
    )

    with get_connection() as conn:
        storage.initialize(conn, creation_schema)

    actions = {
        '1': action_zad_all, # action_find_by_zagol,
        '2': action_add_zad,
        '3': action_redact_zad,
        '4': action_end_zad,
        '5': action_restart_zad,
        'm': action_show_menu,
        'q': action_exit
    }

    action_show_menu()

# метод get не завершит программу при ошибочном вводе, он обрезает ошибочный ввод 
    while True:
        cmd = input('\n Введите команду: ')
        action = actions.get(cmd)
        if action:
            action()
        else:
            print('Неизвестная команда')
# def menu():
#     loop = True
#     while loop == True:
#         print(
#             '\n Ежедневник. Выберите действие:\n\n'
#             ' 1 - Вывести список задач\n'
#             ' 2 - Добавить задачу\n'
#             ' 3 - Отредактировать задачу\n'
#             ' 4 - Завершить задачу\n'
#             ' 5 - Начать задачу сначала\n'
#             ' 0 - Выход'
#         )
#         vvod = input('\n Введите число: ')

#         if vvod == '1':
#             spizad()
#         elif vvod == '2':
#             print('\n Ввввжух и добавляю задачу\n')
#         elif vvod == '3':
#             print('\n Ввввжух и редактирую задачу\n')
#         elif vvod == '4':
#             print('\n Ввввжух и завершаю задачу\n')
#         elif vvod == '5':
#             print('\n Ввввжух и начинаю задачу сначала\n')
#         elif vvod == '0':
#             print('\n Ввввжух и выхожу\n')
#             loop = False
#         else:
#             print('\n Неизвестная команда. Попробуй снова. Я знаю ты сможешь!\n')

# def spizad():
#     loop2 = True
#     while loop2 == True:
#         print(
#             '\n Список задач. Выберите действие:\n\n'
#             ' 1 - За день\n'
#             ' 2 - За неделю\n'
#             ' 3 - За месяц\n'
#             ' 0 - Вернуться в главное меню'
#         )
#         vvod2 = input('\n Введите число: ')

#         if vvod2 == '1':
#             #print('\n Ввввжух и вывожу список задач за день\n')
#             zaden()
#         elif vvod2 == '2':
#             print('\n Ввввжух и вывожу список задач за неделю\n')
#         elif vvod2 == '3':
#                 print('\n Ввввжух и вывожу список задач за месяц\n')
#         elif vvod2 == '0':
#             print('\n Ввввжух и возвращаюсь в главное меню\n')
#             loop2 = False
#         else:
#             print('\n Неизвестная команда. Попробуй снова. Я знаю ты сможешь!\n')

# def zaden():
#     loop3 = True
#     while loop3 == True:
#         print(
#             '\n Список задач. За день. Выберите действие:\n\n'
#             ' 1 - За сегодня\n'
#             ' 2 - За конкретный день\n'
#             ' 0 - Вернуться назад'
#         )
#         vvod3 = input('\n Введите число: ')

#         if vvod3 == '1':
#             print('\n Ввввжух и вывожу список задач за сегодня\n')
#         elif vvod3 == '2':
#             print('\n Ввввжух и вывожу список задач за конкретный день\n')
#         elif vvod3 == '0':
#             print('\n Ввввжух и возвращаюсь назад\n')
#             loop3 = False
#         else:
#             print('\n Неизвестная команда. Попробуй снова. Я знаю ты сможешь!\n')


if (__name__=="__main__"):
    menu() 
