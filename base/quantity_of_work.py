from database import get_connection
from database2 import *


def work_first_table():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS works
                   (
                       id          SERIAL PRIMARY KEY,
                       title       TEXT,
                       description TEXT,
                       profession  VARCHAR(100),
                       date        timestamp default now(),
                       account_id  int references accounts (id)
                   )
                   """)
    connection.commit()
    cursor.close()
    print("table of works created")

def add_work(title, description, profession):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
                   INSERT INTO works (%s, %s, %s)
                   VALUES (title, description, profession)
                   """, (title, description, profession))
    connection.commit()
    cursor.close()


# work_first_table()
