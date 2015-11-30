"""
To use the database, we need to get a cursor object and pass the SQL statements
to the cursor object to execute them. Then, we should commit the changes.

We are going to create a books table with title, author, price and year columns:
________________________________________________________________________________
>>> cursor = db.cursor()
>>> cursor.execute('''CREATE TABLE books(id INTEGER PRIMARY KEY,
...                   title TEXT, author TEXT, price TEXT, year TEXT)
... ''')
>>> db.commit()
________________________________________________________________________________
Note that the commit function is invoked on the db object, not the cursor object.
