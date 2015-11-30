"""
This chapter is a continuation from 'Connecting to DB,create/drop table and
insert data into a table'.

In the previous chapter, we had the following output when we used the sqlite
shell command line:
________________________________________________________________________________
$ sqlite3 test.db

sqlite> .tables
books

sqlite> .mode column
sqlite> .headers on
sqlite> SELECT * FROM books;
id          title            author      price       year
----------  ---------------  ----------  ----------  -----------
1           Learning Python  Mark Lutz   $36.19      Jul 6, 2013
2           Two Scoops of D  Daniel Gre  $34.68      Feb 1, 2014
3           Python Cookbook  David Beaz  $30.29      May 29, 201
4           The Quick Pytho  Naomi R. C  $16.39      Jan 15, 201
5           Python Testing   David Sale  $38.20      Sep 2, 2014
sqlite>
________________________________________________________________________________

To retrieve data, we need to execute the query against the cursor object and
then use 'fetchone()' to retrieve a single row or 'fetchall()' to retrieve all
the rows.
________________________________________________________________________________
>>> cursor.execute('''SELECT title, author, price FROM books''')
<sqlite3.Cursor object at 0x7f1d2717d650>

>>> book1 = cursor.fetchone()
>>> print book1
(u'Learning Python', u'Mark Lutz', u'$36.19')
>>> print(book1[0])
Learning Python
db.cursor().fetchall()
>>> all_cols = cursor.fetchall()

>>> print all_cols
[(u'Two Scoops of Django: Best Practices For Django 1.6', u'Daniel Greenfeld', u'$34.68'), (u'Python Cookbook', u'David Beazley', u'$30.29'), (u'The Quick Python Book', u'Naomi R. Ceder', u'$16.39'), (u'Python Testing', u'David Sale', u'$38.20')]

>>> for col in all_cols:
...     print('{0} : {1}, {2}'.format(col[0], col[1], col[2]))
...
Two Scoops of Django: Best Practices For Django 1.6 : Daniel Greenfeld, $34.68
Python Cookbook : David Beazley, $30.29
The Quick Python Book : Naomi R. Ceder, $16.39
Python Testing : David Sale, $38.20
________________________________________________________________________________

The cursor object works as an iterator, invoking fetchall() automatically:
________________________________________________________________________________
>>> cursor.execute('''SELECT title, author, price, year FROM books''')
<sqlite3.Cursor object at 0x7f1d2717d650>
>>> for col in cursor:
...     # col[0] returns the first column in the query (title), col[1] return
author column.
...     print('{0} : {1}, {2}, {3}'.format(col[0], col[1], col[2], col[3]))
...
Learning Python : Mark Lutz, $36.19, Jul 6, 2013
Two Scoops of Django: Best Practices For Django 1.6 : Daniel Greenfeld, $34.68, Feb 1, 2014
Python Cookbook : David Beazley, $30.29, May 29, 2013
The Quick Python Book : Naomi R. Ceder, $16.39, Jan 15, 2010
Python Testing : David Sale, $38.20, Sep 2, 2014
________________________________________________________________________________
