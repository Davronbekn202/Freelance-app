from account import *
from base.database import get_connection


def has_done(done,description,rate):
   connection = get_connection()
   cursor = connection.cursor
   cursor.execute("""
   insert into (done,description,rate)
   values (%s,%s,%s)
   """,(done,description,rate))
   connection.commit()
   cursor.close()
