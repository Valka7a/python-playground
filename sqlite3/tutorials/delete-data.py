"""
________________________________________________________________________________
>>> delete_book_id = 5
>>> cursor.execute('''DELETE FROM books WHERE id = ?''', (delete_book_id,))
<sqlite3.Cursor object at 0x7f1d2717d650>
>>> db.commit()
________________________________________________________________________________

Let's check the last boot(id = 5) is gone:
________________________________________________________________________________
>>> cursor.execute('''SELECT title, author, price FROM books''')
<sqlite3.Crusor object at 0x7f1d2717d650>
[(u'Learning Python', u'Mark Lutz', u'$36.19'), (u'Two Scoops of Django: Best Practices For Django 1.6', u'Daniel Greenfeld', u'$34.68'), (u'Python Cookbook', u'David Beazley', u'$30.29'), (u'The Quick Python Book', u'Naomi R. Ceder', u'$19.99')]
________________________________________________________________________________

Yes, it's not there anymore.
