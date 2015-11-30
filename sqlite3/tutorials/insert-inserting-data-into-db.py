i"""
To insert data we use the cursor to execute the query. In this example we are
going to insert two books in the database, their information will stored in
python variables.
________________________________________________________________________________
>>> db.close()
>>> import sqlite3
>>> db = sqlite3.connect('data/test.db')
>>> cursor = db.sursor()
>>> cursor.execute('''CREATE TABLE book(id INTEGER PRIMARY KEY,
...                     title TEXT, author TEXT, price TEXT, year TEXT)
...                ''')
>>> db.commit()

>>> import sqlite3
>>> db = sqlite3.connect('data/test.db')
>>> cursor = db.cursor()
>>> title1 = 'Learning Python'
>>> author1 = 'Mark Lutz'
>>> price1 = '$36.19'
>>> year1 = 'Jul 6, 2013'
>>>
>>> title2 = 'Two Scoops of Django: Best Practices For Django 1.6'
>>> autor2 = 'Daniel Greenfeld'
>>> price2 = '$34.68'
>>> year2 = 'Feb 1, 2014'

>>> cursor.execute('''INSERT INTO books(title, author, price, year)
...                   VALUES(?,?,?,?)''', (title1, author1, price1, year1))

>>> cursor.execute('''INSERT INTO books(title, author, price, year)
...                   VALUES(?,?,?,?)''', (title2, author2, price2, year2))

>>> db.commit()
________________________________________________________________________________
Note: If we need values from Python variables it is recommended to use "?"
placeholder. Never use string operations or concatenation to make your queries
because it very insecure.

The values of the Python variables are passed inside a tuple.

If we have more books to insert, we can continue. But this time, we'll do it
another way: passing a dictionary using the ":keyname" placeholder:
________________________________________________________________________________
>>> title3 = 'Python Cookbook'
>>> author3 = 'David Beazley'
>>> price3 = '$30.29'
>>> year3 =  'May 29, 2013'

>>> cursor.execute('''INSERT INTO books(title, author, price, year)
...                   VALUES(:title, :author, :price, :year)''',
...                   {'title':title3, 'author':author3, 'price':price3, 'year':year3})
<sqlite3.Cursor object at 0x7f1d2717d650>
>>>
>>> db.commit()
________________________________________________________________________________
If we need to insert several users, we can use executemany and a list with the
tuples:
________________________________________________________________________________
>>> title4 = 'The Quick Python Book'
>>> author4 = 'Naomi R. Ceder'
>>> price4 = '$16.39'
>>> year5 = 'Jan 15, 2010'
>>>
>>> title5 = 'Python Testing'
>>> author5 = 'David Sale'
>>> price5 = '$38.20'
>>> year5 = 'Sep 2, 2014'

>>> books = [(title4, author4, price4, year4),
             (title5, author5, price5, year5)]
>>> cursor.executemany('''INSERT INTO books(title, author, price, year) VALUES(?,?,?,?)''' books)
>>> db.commit()

cursor.executemany('''INSERT INTO books(title, author, price, year) VALUES(?,?,?,?)''', books)
