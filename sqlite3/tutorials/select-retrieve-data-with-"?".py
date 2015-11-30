"""
We can use the ? placeholder to retrieve data with conditions:
________________________________________________________________________________
>>> book_id = 3
>>> cursor.execute('''SELECT title, author, price FROM books WHERE id=?''',(book_id,))
<sqlite3.Cursor object at 0x7f1d2717d650>
>>> book = cursor.fetchone()
>>> print(book)
(u'Python Cookbook', u'David Beazley', u'$30.29')
________________________________________________________________________________
