"""
Another way of creating db is to use the sqlite3 command line tool:
________________________________________________________________________________
$ ls
$ sqlite3 test.db
SQLite version 3.7.17 2013-05-20 00:56:22
Enter ".help" for instructions
Enter SQL statements terminated with a ";"
sqlite> .tables
sqlite> .exit
$ ls
test.db
________________________________________________________________________________
The .tables command gives a list of tables in the test.db database. We don't have
any tables now. The .exit command terminates the interactive session of the
sqlite3 command line tool.
