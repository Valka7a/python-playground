import sqlite3

class Db(object):

    def __init__(self):
        self.db = sqlite3.connect('data/test.db')

    def get_conn(self):
        return self.db
