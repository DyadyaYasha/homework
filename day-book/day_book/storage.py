import menu
import os.path as Path
import sqlite3

SQL_SELECT_ALL = """
    SELECT id, day, month, zagolovok, zadacha, status
    FROM daybook
""" 

menu.menu()

def connect(db_name=None):
    if db_name is None:
        db_name = 'daybook.sqlite'

    conn = sqlite3.connect(db_name)
    # магия

    return conn

def initialize(conn, creation_schema):
    with conn, open(creation_schema) as f:
        conn.executescript(f.read())


def add_zad(conn, zad):
    """Сохраняет новую задачу в базу"""


def zad_all(conn):
    """Возвращает все задачи из базы"""


def zad_by_pk(conn, pk):
    """Возвращает задачу по первичному ключу"""   


def zad_by_zagol(conn, zagol):
    """Возвращает задачу по короткому заголовоку"""


def zad_by_dm(conn, day):
    """Возвращает задачи по конкретному деню""" 

def zad_by_dm(conn, day, month):
    """Возвращает задачи по дате день + месяц""" 





