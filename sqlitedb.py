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
            gender varchar(12),
            active_from DATETIME,
            active_to DATETIME)'''
        self.cur.execute(sql)
        sql = '''create table if not exists Category 
            (ID INTEGER PRIMARY KEY AUTOINCREMENT,
            name varchar(50))'''
        self.cur.execute(sql)
        sql = '''create table if not exists Goods 
             (ID INTEGER PRIMARY KEY AUTOINCREMENT,
             Category_ID INTEGER NOT NULL REFERENCES Categry(ID),
             name varchar(50))'''
        self.cur.execute(sql)
        sql = '''create table if not exists Inc_records 
            (ID INTEGER PRIMARY KEY AUTOINCREMENT,
            User_ID INTEGER NOT NULL REFERENCES Users(ID),
            summ integer,
            com varchar(50),
            date_rec DATETIME)'''
        self.cur.execute(sql)
        sql = '''create table if not exists Dec_records 
            (ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Goods_ID INTEGER NOT NULL REFERENCES Goods(ID),
            User_ID INTEGER NOT NULL REFERENCES Users(ID),
            summ integer,
            com varchar(50),
            date_rec DATETIME)'''
        self.cur.execute(sql)
        self.conn.commit()

    def add_user(self, user):
        print(user)
        self.cur.execute("INSERT INTO Users(full_name, age, gender, active_from) "
                         "VALUES('%s', %d, '%s', CURRENT_TIMESTAMP)"
                         % (user['full_name'], user['age'], user['gender']))
        self.conn.commit()
        self.cur.execute("SELECT ID FROM Users WHERE full_name='%s'" % user['full_name'])
        return self.cur.fetchone()

    def delete_user(self, idx):
        sel = '''UPDATE Users set active_to=CURRENT_TIMESTAMP where id = %d''' % (idx)
        self.cur.execute(sel)
        self.conn.commit()

    def get_all_users(self):
        self.cur.execute("SELECT * FROM Users where active_to is null")
        return self.cur.fetchall()

    def get_all_cat(self):
        self.cur.execute("SELECT * FROM Category")
        return self.cur.fetchall()

    def get_all_goods_in_cat(self, cat):
        self.cur.execute("SELECT * FROM Goods where Category_ID=%s"%cat)
        return self.cur.fetchall()

    def add_record(self, good_id, user_id, summ, comment=None):
        self.cur.execute("INSERT INTO Dec_records(Goods_ID, User_ID, summ, com, date_rec) "
                         "VALUES('%d', %d, '%d', '%s', CURRENT_TIMESTAMP)"
                         % (good_id, user_id, summ, comment))
        self.conn.commit()

    def select_report_1(self):
        self.cur.execute("select u.full_name, c.name, sum(summ) "
                         "from Dec_records dr, Category c, Goods g, Users u "
                         "where dr.date_rec > '2021-02-16 00:00:00' "
                         "and dr.Goods_ID=g.ID "
                         "and g.Category_ID=c.ID "
                         "and u.ID=dr.User_ID "
                         "group by u.full_name, c.name")
        return self.cur.fetchall()

    def select_report_2(self):
        self.cur.execute("select c.name, sum(dr.summ) "
                         "from Dec_records dr, Category c, Goods g "
                         "where dr.Goods_ID=g.ID "
                         "and g.Category_ID=c.ID "
                         "group by c.name;")
        return self.cur.fetchall()

    def select_report_3(self):
        self.cur.execute("select g.name, max(dr.summ) "
                         "from Dec_records dr, Category c, Goods g "
                         "where dr.Goods_ID=g.ID and g.Category_ID=c.ID "
                         "group by c.name;")
        return self.cur.fetchall()


