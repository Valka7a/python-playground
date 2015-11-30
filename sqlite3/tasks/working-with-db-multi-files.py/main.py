from db import *
from user_model import *

conn = Db().get_conn()
user_model = UserModel(conn)

user_model.create({
  'username': "fre2ak",
  'email': "fretwoak@gmail.com",
  'first_name': "Ivo",
  'last_name': "Dukov",
  'age': 21,
  'role': "user",
  'password': "p455w0rD!"
})
