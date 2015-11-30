"""
To connect to the database, we can use sqlite3.connect function by passing the
name of a life to open or create it:
________________________________________________________________________________
>>> import sqlite3
>>> db = sqlite3.connect('data/test.db')
________________________________________________________________________________
We can use the argument ":memory:" to create a temporary DB in the RAM:
________________________________________________________________________________
>>> import sqlite3
>>> dbm = db = sqlite3.connect(':memory:')
________________________________________________________________________________
When we are done working with the DB we need to close the connection:
________________________________________________________________________________
>>> db.close()
>>> dbm.close()
________________________________________________________________________________
