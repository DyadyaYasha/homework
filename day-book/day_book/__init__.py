import os.path as Path
import sys

from day_book import storage

get_connection = lambda : storage.connect('daybook.sqlite')


def action_add_zad():
    """Добавить задачу"""
    zagolovok = vvod_zagol()
    zadacha = vvod_zad()
    with get_connection() as conn:
        zad = storage.add_zad(conn, zadacha, zagolovok)
    if not zadacha:
        return
    return zad


def vvod_zagol():
    while True:
        zagol = input('\n Введите заголовок: \n')
        if zagol:
            return zagol


def vvod_zad():
    while True:
        zad = input('\n Введите задачу: \n')
        if zad:
            return zad


def action_find_by_zagol():
    """Найти задачу по заголовку"""
    zagol = input('Введите заголовок задачи: ')
    if zagol:
        with get_connection() as conn:
            row = storage.zad_by_zagol(conn, zagol)
        if row:
            zad = row.get('zadacha')
            print('Ваша задача: {}'.format(zad)) # format вставляет то что нам нужно в {}
        else:
            print('Заголовок "{}" не существует'.format(zagol))



def action_zad_all():
    """Вывести все задачи"""
    with get_connection() as conn:
        rows = storage.zad_all(conn)

    template = '\n Задача № {row[id]} - Заголовок "{row[zagolovok]}" - Текст "{row[zadacha]}" - Статус "{row[status]}" - Дата создания {row[created]}'
    for row in rows:
        print(template.format(row=row))


def action_redact_zad():
    """Редактировать задачу"""
    pk = input('Введите номер задачи: ')

    if pk:
        with get_connection() as conn:
            zad = storage.zad_by_pk(conn, pk)

        if zad:
            rezad = input('\n Введите исправления: ')
            with get_connection() as conn:
                zad = storage.vary_zad(conn, pk, rezad)
                print('\n Задача № {} исправлена'.format(pk))
        else:
            print('Задача № {} не существует'.format(pk))

def action_redact_zagol():
    """Редактировать заголовок"""
    pk = input('Введите номер задачи: ')

    if pk:
        with get_connection() as conn:
            zag = storage.zad_by_pk(conn, pk)

        if zag:
            rezag = input('\n Введите исправленный заголовок: ')
            with get_connection() as conn:
                zag = storage.vary_zagol(conn, pk, rezag)
                print('\n Заголовок задачи № {} исправлен'.format(pk))
        else:
            print('Задача № {} не существует'.format(pk))


def action_end_zad():
    """Закончить задачу"""
    pk = input('Введите номер задачи: ')

    if pk:
        with get_connection() as conn:
            zad = storage.zad_by_pk(conn, pk)

        if zad:
            stat = 'Закончена'
            with get_connection() as conn:
                zad = storage.vary_status(conn, pk, stat)
                print('\n Задача № {} закончена'.format(pk))
        else:
            print('Задача № {} не существует'.format(pk))


def action_restart_zad():
    """Начать задачу сначала"""
    pk = input('Введите заголовок задачи: ')

    if pk:
        with get_connection() as conn:
            zad = storage.zad_by_pk(conn, pk)

        if zad:
            stat = "Не закончена"
            with get_connection() as conn:
                zad = storage.vary_status(conn, pk, stat)
                print('\n Статус задачи № {} изменён на "Не закончена"'.format(zagol))
        else:
            print('\n Задача № {} не существует'.format(pk))


def action_show_menu():
    """Показать меню"""
    print("""
 Ежедневник. Выберите действие:

 1. - Вывести список задач
 2. - Добавить задачу
 3. - Отредактировать задачу
 4. - Завершить задачу
 5. - Начать задачу сначала
 6. - Найти задачу по заголовку
 7. - Отредактировать заголовок
 m. - Показать меню
 q. - Выйти""")


def action_exit():
    """Выйти из программы"""
    sys.exit(0)



def main():
    creation_schema = Path.join(
        Path.dirname(__file__), 'schema.sql'
    )

    with get_connection() as conn:
        storage.initialize(conn, creation_schema)

    actions = {
        '1': action_zad_all,
        '2': action_add_zad,
        '3': action_redact_zad,
        '4': action_end_zad,
        '5': action_restart_zad,
        '6': action_find_by_zagol,
        '7': action_redact_zagol,
        'm': action_show_menu,
        'q': action_exit
    }

    action_show_menu()

    while True:
        cmd = input('\n Введите команду: ')
        action = actions.get(cmd)
        if action:
            action()
        else:
            print('Неизвестная команда')