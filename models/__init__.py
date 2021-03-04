import pymysql.cursors
import os

connection = pymysql.connect(host="localhost", user='root', password="sample", database='dpm');

def initDB():
    print(os.getcwd())
    with open("models/sql-init.sql", "r") as file:
        with connection.cursor() as cursor:
            sql = file.read();
            cursor.execute(sql)
            connection.commit()

