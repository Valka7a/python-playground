"""
Now, we want to update data in the table. Let's switch the price of the 4th
book(id = 4).
________________________________________________________________________________
>>> newPrice = '$19.99'
>>> book_id = 4
>>> cursor.execute('''UPDATE books SET price = ? WHERE id = ?''', (newPrice, book_id))
<sqlite3.Cursor object at 0x7f1d2717d650>
________________________________________________________________________________

We can check if the price of the 4th(book_id = 4) book has been updated from
$16.39 to $19.99:
________________________________________________________________________________
>>> cursor.execute('''SELECT title, author, price FROM books''')
<sqlite3.Cursor object at 0x7f1d2717d650>
>>> all_books = cursor.fetchall()
>>> print(all_books)
[(u'Learning Python', u'Mark Lutz', u'$36.19'), (u'Two Scoops of Django: Best Practices For Django 1.6', u'Daniel Greenfeld', u'$34.68'), (u'Python Cookbook', u'David Beazley', u'$30.29'), (u'The Quick Python Book', u'Naomi R. Ceder', u'$19.99'), (u'Python Testing', u'David Sale', u'$38.20')]
________________________________________________________________________________
"""
