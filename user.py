import sqlitedb


class User:
    def __init__(self, fullname, age, gender):
        self.full_name = str(fullname)
        self.age = int(age)
        self.gender = str(gender)

    def add_user(self):
        sdb = sqlitedb.Sqlite_DB()
        return sdb.add_user(self.get_user())

    def get_user(self):
        user = {}
        user['full_name'] = self.full_name
        user['age'] = self.age
        user['gender'] = self.gender
        return user
