import sqlite3
import os

if not os.path.exists('database.db'):
    f = open('schema.sql','r',encoding = 'utf-8')
    sql_schema = f.read()
    f.close()
    f = open('init.sql','r', encoding = 'utf-8')
    sql_init = f.read()
    f.close()

    conn = sqlite3.connect('database.db')
    conn.cursor().executescript(sql_schema)
    conn.cursor().executescript(sql_init)
    conn.commit()
