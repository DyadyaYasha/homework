import os.path as Path
import sqlite3

SQL_SELECT_ALL = """
    SELECT id, zagolovok, zadacha, status, created
    FROM daybook
""" 

SQL_SELECT_ZAD_BY_PK = SQL_SELECT_ALL + " WHERE id=?"

SQL_SELECT_ZAD_BY_FULLTEXT = SQL_SELECT_ALL + " WHERE zadacha=?"

SQL_SELECT_ZAD_BY_ZAGOLOVOK = SQL_SELECT_ALL + " WHERE zagolovok=?"

SQL_SELECT_ZAD_BY_STATUS = SQL_SELECT_ALL + " WHERE status=?"

SQL_INSERT_ZAD = """
    INSERT INTO daybook (zadacha, zagolovok) VALUES (?, ?)
"""

SQL_UPDATE_ZAD = """
    UPDATE daybook SET zadacha=? WHERE id=?
"""

SQL_INSERT_ZAGOLOVOK = """
    INSERT INTO daybook (zagolovok) VALUES (?)
"""

SQL_UPDATE_ZAGOLOVOK = """
    UPDATE daybook SET zagolovok=? WHERE id=?
"""

SQL_UPDATE_STATUS = """
    UPDATE daybook SET status=? WHERE id=?
"""

# обязательно условие WHERE и то что должно обновиться, без него обновится все в таблице

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def connect(db_name):
    if db_name is None:
        db_name = 'daybook.sqlite'
    conn = sqlite3.connect(db_name)
    conn.row_factory = dict_factory
    return conn


def initialize(conn, creation_schema):
    with conn, open(creation_schema) as f:
        conn.executescript(f.read())


def add_zad(conn, zadacha, zagolovok):
    """Сохраняет новую задачу в базу"""
    cursor = conn.execute(SQL_INSERT_ZAD, (zadacha, zagolovok))


def zad_all(conn):
    """Возвращает все задачи из базы"""
    with conn:
        cursor = conn.execute(SQL_SELECT_ALL) 
        return cursor.fetchall()


def zad_by_pk(conn, pk):
    """Возвращает задачу по первичному ключу"""
    with conn:
        cursor = conn.execute(SQL_SELECT_ZAD_BY_PK, (pk, ))
        return cursor.fetchone()


def zad_by_zagol(conn, zagol):
    """Возвращает задачу по заголовоку"""
    with conn:
        cursor = conn.execute(SQL_SELECT_ZAD_BY_ZAGOLOVOK, (zagol, ))
        return cursor.fetchone()


def zad_by_status(conn, status):
    """Возвращает задачи по статусу"""
    with conn:
        cursor = conn.execute(SQL_SELECT_ZAD_BY_STATUS, (status, ))
        return cursor.fetchall()


def vary_zad(conn, pk, zadacha):
    with conn:
        conn.execute(SQL_UPDATE_ZAD, (zadacha, pk))


def vary_zagol(conn, pk, zagolovok):
    with conn:
        conn.execute(SQL_UPDATE_ZAGOLOVOK, (zagolovok, pk))


def vary_status(conn, pk, status):
    with conn:
        conn.execute(SQL_UPDATE_STATUS, (status, pk))







