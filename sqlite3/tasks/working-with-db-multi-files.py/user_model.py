class UserModel(object):

    def __init__(self, conn):
        self.conn = conn
        self.create_table()

    def create_table(self):
        self.conn.cursor().execute('''CREATE TABLE IF NOT EXISTS users(
                                    id INTEGER PRIMARY KEY  AUTOINCREMENT,
                                    username    TEXT    UNIQUE  NOT NULL,
                                    email       TEXT    UNIQUE  NOT NULL,
                                    first_name  TEXT            NOT NULL,
                                    last_name   TEXT            NOT NULL,
                                    age         INT             NOT NULL,
                                    role        TEXT            NOT NULL,
                                    password    TEXT            NOT NULL,
                                    date_create DATETIME DEFAULT CURRENT_TIMESTAMP,
                                    date_updated DATETIME DEFAULT CURRENT_TIMESTAMP)
                                    ''')

        self.conn.commit()

    def find_all(self):
        pass

    def find_by(self, params):
        pass

    def find_one(self, params):
        pass

    def create(self, params):
        self.conn.cursor().execute('''INSERT INTO users(username, email, first_name,
                                last_name, age, role, password)
                                VALUES(:username, :email, :first_name, :last_name,
                                :age, :role, :password)''', params)

        self.conn.commit()


    def update(self, id, params):
        pass

    def delete(self, id):
        pass
