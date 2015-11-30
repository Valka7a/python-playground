import sqlite3

class Db(object):

    def __init__(self):
        self.db = sqlite3.connect('data/test.db')

    def get_conn(self):
        return self.db


class User(object):

    def __init__(self, params):
        self.id = params[0]
        self.username = params[1]
        self.email = params[2]
        self.first_name = params[3]
        self.last_name = params[4]
        self.age = params[5]
        self.role = params[6]
        self.date_create = params[8]
        self.date_updated = params[9]

    def __str__(self):
        params = [
                    str(self.id),
                    self.username,
                    self.email,
                    self.first_name,
                    self.last_name,
                    str(self.age),
                    self.role,
                    self.date_create,
                    self.date_updated
                    ]

        return ' '.join(params)


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
        users = self.conn.cursor().execute("SELECT * FROM users").fetchall()
        return map(lambda user_params: User(user_params), users)

    def find_by(self, params):
        string = []

        for field in params.keys():
            if not string:
                string.append("SELECT * FROM users WHERE " + field + "= ?")
            else:
                string.append(" AND " + field + "= ?")

        word = ''.join(string)

        users = self.conn.cursor().execute(word, params.values()).fetchall()

        return map(lambda user_params: User(user_params), users)


    def find_one(self, id):
        users_params = self.conn.cursor().execute("SELECT * FROM users WHERE id=?",
                                            str(id)).fetchone()
        return User(users_params)

    def create(self, params):
        self.conn.cursor().execute('''INSERT INTO users(username, email, first_name,
                                last_name, age, role, password)
                                VALUES(:username, :email, :first_name, :last_name,
                                :age, :role, :password)''', params)

        self.conn.commit()


    def update(self, id, params):
        string = ['UPDATE users SET ']

        for field in params.keys():
            string.append(field + '= ?')

        string.append(' WHERE id= ?')


        values = params.values()
        values.append(int(id))

        self.conn.cursor().execute(''.join(string), values)

        self.conn.commit()


    def delete(self, id):
        self.conn.cursor().execute("DELETE FROM users WHERE id= ?", [id])

        self.conn.commit()


class Book(object):

    def __init__(self, params):
        self.id = params[0]
        self.name = params[1]
        self.author = params[2]
        self.publishing_house = params[3]
        self.price = params[4]
        self.year = params[5]
        self.date_create = params[6]
        self.date_updated = params[7]


    def __str__(self):
        params = [
                    str(self.id),
                    self.name,
                    self.author,
                    self.publishing_house,
                    self.price,
                    self.year,
                    self.date_create,
                    self.date_updated
                    ]

        return ' '.join(params)


class BookModel(object):

    def __init__(self, conn):
        self.conn = conn
        self.create_table()


    def create_table(self):
        self.conn.cursor().execute('''CREATE TABLE IF NOT EXISTS books(
                                    id INTEGER PRIMARY KEY  AUTOINCREMENT,
                                    name                TEXT    UNIQUE  NOT NULL,
                                    author              TEXT            NOT NULL,
                                    publishing_house    TEXT            NOT NULL,
                                    price               TEXT            NOT NULL,
                                    year                TEXT            NOT NULL,
                                    date_create DATETIME DEFAULT CURRENT_TIMESTAMP,
                                    date_updated DATETIME DEFAULT CURRENT_TIMESTAMP)
                                    ''')

        self.conn.commit()


    def find_all(self):
        users = self.conn.cursor().execute("SELECT * FROM books").fetchall()
        return map(lambda user_params: Book(user_params), users)

    def find_by(self, params):
        string = []

        for field in params.keys():
            if not string:
                string.append("SELECT * FROM books WHERE " + field + "= ?")
            else:
                string.append(" AND " + field + "= ?")

        word = ''.join(string)

        users = self.conn.cursor().execute(word, params.values()).fetchall()

        return map(lambda user_params: Book(user_params), users)

    def find_one(self, id):
        users_params = self.conn.cursor().execute("SELECT * FROM books WHERE id=?",
                                                    str(id)).fetchone()

        return Book(users_params)

    def create(self, params):
        self.conn.cursor().execute('''INSERT INTO books(name, author,
                                    publishing_house, price, year)
                                    VALUES(:name, :author, :publishing_house,
                                    :price, :year)''', params)

        self.conn.commit()


    def update(self, id, params):
        string = ['UPDATE books SET ']

        for field in params.keys():
            string.append(field + '= ?')

        string.append(' WHERE id= ?')

        values = params.values()
        values.append(int(id))

        self.conn.cursor().execute(''.join(string), values)

        self.conn.commit()


    def delete(self, id):
        self.conn.cursor().execute("DELETE FROM books WHERE id= ?", [id])

        self.conn.commit()


class Model(object):

    def __init__(self, conn):
        self.conn = conn
        self.validate()
        self.create_table()

    def validate(self):
        if self.table == '' or self.entity_class == "":
            raise Error("Must specify table and entity_class property of the model.")

    def creater_table(self):
        raise NotImplementedError()

    def find_all(self):
        items = self.conn.cursor().execute("SELECT * FROM " + self.table).fetchall()
        return map(lambda item_params: globals()[self.entity_class](item_params), items)

    def find_by(self, params):
        query_string = []

        for field in params.keys():
            if not string:
                query_string.append("SELECT * FROM " + self.table + " WHERE " + field + "= ?")
            else:
                query_string.append(" AND " + field + "= ?")

        items = self.conn.cursor().execute(''.join(query_string), params.values()).fetchall()

        return map(lambda item_params: globals()[self.entity_class](item_params), items)


    def find_one(self, id):
        item_params = self.conn.cursor().execute("SELECT * FROM " + self.table +
                                                " WHERE id = ?", [id]).fetchone()
        return globals()[self.entity_class](item_params)

    def create(self, params):
    query_string = [
        "INSERT INTO ",
        self.table,
        "("
    ]

    fields = params.keys()
    query_string.append(", ".join(fields))
    query_string.append(") VALUES (:")
    query_string.append(", :".join(fields))
    query_string.append(")")

    self.conn.cursor().execute(''.join(query_string), params)
    self.conn.commit()

    def update(self, id, params):
    query_string = [
        "UPDATE ",
        self.table,
        " SET "]

    for field in params.keys():
        query_string.append(field + '= ?')

    query_string.append(' WHERE id= ?')

    values = params.values()
    values.append(int(id))

    self.conn.cursor().execute(''.join(query_string), values)
    self.conn.commit()

    def delete(self, id):
        self.conn.cursor().execute("DELETE FROM " + self.table + " WHERE id= ?", [id])
        self.conn.commit()





conn = Db().get_conn()
book_model = BookModel(conn)


book_model.create({'name':'How to earn from internet',
                'author':'Alexander Nenov',
                'publishing_house': 'Factory for books',
                'price':'40,00lv', 'year':'2013'})

books = book_model.find_all()

for i in books:
    print i

"""
conn = Db().get_conn()
user_model = UserModel(conn)

users = user_model.find_all()

for user in users:
    print user
"""


"""
for user in users:
    print user


user_model.delete(7)

users = user_model.find_all()

for user in users:
    print "NEW:", user
"""

# user_model.update(1, {'username':'rainbowa'})


# for user in users:
#  print user


# user_by_id = user_model.find_one(1)

# print user_by_id.username




# user = {'username':'rainbowa', 'age': 21}
# user_by = user_model.find_by(user)




# print user_by_id

# for user in users:
#    print ('{0} - {1} - {2} - {3} - {4} - {5} - {6}'.format(user[0], user[1],
#                                user[2], user[3], user[4], user[5], user[6]))

"""
user_model.create({
  'username': "rainbowa2",
  'email': "rainbowa2@gmail.com",
  'first_name': "Ivo",
  'last_name': "Dukov",
  'age': 21,
  'role': "user",
  'password': "p455w0rD!"
})
"""
