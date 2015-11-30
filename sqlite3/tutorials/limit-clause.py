"""
The SQLite LIMIT clause is used to limit the data amount returned by the SELECT
statement.
"""

# Syntax:
"""
The basic syntax of SELECT statement with LIMIT clause is as follows:
________________________________________________________________________________
SELECT column1, column2, columnN
FROM table_name
LIMIT [no of rows]
________________________________________________________________________________

Following is the syntax of LIMIT clause when it is used along with OFFSET clause:
________________________________________________________________________________
SELECT column1, column2, columnN
FROM table_name
LIMIT [no of rows] OFFSET [row num]
________________________________________________________________________________

SQLite engine will return rows starting from the next row to the given OFFSET as
shown below in the last example.
"""

# Example:
"""
Consider COMPANY table is having the following records:
________________________________________________________________________________
ID      Name        Age     ADDRESS         SALARY
-----   ----------  ------  ------------    -----------
1       Paul        32      California      20000.0
2       Allen       25      Texas           15000.0
3       Teddy       23      Norway          20000.0
4       Mark        25      Rich-Mond       65000.0
5       David       27      Texas           85000.0
6       Kim         22      South-Hall      45000.0
7       James       24      Houston         10000.0
________________________________________________________________________________

Following is an example, which limits the row in the table according to the number
of rows you want to fetch from table:
________________________________________________________________________________
sqlite> SELECT * FROM COMPANY LIMIT 6;
________________________________________________________________________________

This would produce the following result:
________________________________________________________________________________
ID      Name        Age     ADDRESS         SALARY
-----   ----------  ------  ------------    -----------
1       Paul        32      California      20000.0
2       Allen       25      Texas           15000.0
3       Teddy       23      Norway          20000.0
4       Mark        25      Rich-Mond       65000.0
5       David       27      Texas           85000.0
6       Kim         22      South-Hall      45000.0
________________________________________________________________________________

But in certain situations, you may need to pick up a set of records from a particular
offset. Here is an example, which picks up 3 records starting from 3rd position:
________________________________________________________________________________
sqlite> SELECT * FROM COMPANY LIMIT 3 OFFSET 2;
________________________________________________________________________________

This would produce the following result:
________________________________________________________________________________
ID      Name        Age     ADDRESS         SALARY
-----   ----------  ------  ------------    -----------
3       Teddy       23      Norway          20000.0
4       Mark        25      Rich-Mond       65000.0
5       David       27      Texas           85000.0
________________________________________________________________________________
