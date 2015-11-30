"""
Let's see what we've done so far using sqlite command shell:
________________________________________________________________________________
$ sqlite3 test.db
SQLite version 3.7.17 2013-05-20 00:56:22
Enter ".help" for instructions
Enter SQL statements terminated with a ";"

sqlite> .tables
books

sqlite> SELECT * FROM books;
1|Learning Python|Mark Lutz|$36.19|Jul 6, 2013
2|Two Scoops of Django: Best Practices For Django 1.6|Daniel Greenfeld|$34.68|Feb 1, 2014
3|Python Cookbook|David Beazley|$30.29|May 29, 2013
4|The Quick Python Book|Naomi R. Ceder|$16.39|Jan 15, 2010
5|Python Testing|David Sale|$38.20|Sep 2, 2014

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

Note that we modified the way the data is displayed in the console.
We used the column mode and turend on the headers.
