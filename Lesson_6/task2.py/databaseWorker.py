import sqlite3
from sqlite3 import Error


def init_conn(path):
    conn = None
    try:
        conn = sqlite3.connect(path)
        print ("Connection established!")
    except Error as e:
        print (e)
        print ("Connection failed!")
    return conn    

def init_tables(connection):
    sql = "CREATE TABLE IF NOT EXISTS options(name text NOT NULL, text text NOT NULL);"
    connection.execute(sql)

def prepareDb(name):
    conn = init_conn(name)
    init_tables(conn)
    conn.close()

def getText(name):
    connection = init_conn(name)
    sql = "SELECT * FROM options;"
    cursor = connection.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    connection.close()
    html = ""
    for row in rows:
        html+=f"<p>{row[0]}: {row[1]} </p>"
    return html


def cleardb():
    connection = init_conn("options.db")
    cursor = connection.cursor()
    cursor.execute("DELETE from options where 1")
    connection.commit()
    connection.close()