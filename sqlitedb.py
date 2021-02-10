import os
import sqlite3

DB_FILE = "base.db"


class Sqlite_DB:
    def __init__(self):
        b = False
        if not os.path.isfile(DB_FILE):
            b = True
        self.conn = sqlite3.connect(DB_FILE)
        self.cur = self.conn.cursor()
        if b:
            self.create_db()

    def create_db(self):
        sql = '''create table if not exists Users 
            (ID INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name varchar(50), 
            age integer, 
            gender varchar(12))'''
        self.cur.execute(sql)
        sql = '''create table if not exists Category 
            (ID INTEGER PRIMARY KEY AUTOINCREMENT,
            name varchar(50))'''
        self.cur.execute(sql)
        sql = '''create table if not exists goods 
             (ID INTEGER PRIMARY KEY AUTOINCREMENT,
             Category_ID INTEGER NOT NULL REFERENCES Categry(ID),
             name varchar(50))'''
        self.cur.execute(sql)
        sql = '''create table if not exists Income_sources 
            (ID INTEGER PRIMARY KEY AUTOINCREMENT,
            name varchar(50),
            summ integer)'''
        self.cur.execute(sql)
        sql = '''create table if not exists Cost 
            (ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Category_ID INTEGER NOT NULL REFERENCES Categry(ID),
            name varchar(50),
            summ integer)'''
        self.cur.execute(sql)
        self.conn.commit()

    def add_user(self, user):
        print(user)
        self.cur.execute("INSERT INTO Users(full_name, age, gender) VALUES('%s', %d, '%s')" % (user['full_name'], user['age'], user['gender']))
        self.conn.commit()
        self.cur.execute("SELECT ID FROM Users WHERE full_name='%s'" % user['full_name'])
        return self.cur.fetchone()

    def get_all_users(self):
        self.cur.execute("SELECT * FROM Users")
        return self.cur.fetchall()
