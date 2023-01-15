import sqlite3
from datetime import datetime


def init_conn(path):
    conn = None
    try:
        conn = sqlite3.connect(path)
        print ("Connection established!")
    except Error as e:
        print (e)
        print ("Connection failed!")
    return conn    

db = init_conn("chat.db")
sql = db.cursor()
sql.execute("""CREATE TABLE IF NOT EXISTS chat (
    login text NOT NULL,
    message text NOT NULL,
    time text NOT NULL
    )""")
db.commit()
db.close()

def addMessage(login,message,time):
    db = init_conn("chat.db")
    sql = db.cursor()
    sql.execute(f"INSERT INTO chat VALUES (?,?,?)",(login,message,time))
    db.commit()
    db.close()

def getMessage():
    db = init_conn("chat.db")
    sql = db.cursor()
    sql.execute(f"SELECT * FROM chat")
    rows=sql.fetchall()
    db.close()
    html= ""
    for row in rows:
        html+=f"<p>{row[0]}: {row[1]} <p style='text-align:right'>{row[2]}</p></p>"
    return html

def databaseDel():
    db = init_conn("chat.db")
    sql = db.cursor()
    sql.execute("DELETE from chat where 1")
    db.commit()
    db.close()

def time():
    time = datetime.now()
    time = time.strftime("%Y-%m-%d  %H:%M:%S")
    return time