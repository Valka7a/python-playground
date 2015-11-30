"""
The SQLite GROUP BY clause is used in collaboration with the SELECT statement to
arrange identical data into groups.

The GROUP BY clause follows the WHERE clause in a SELECT statement and precedes
the ORDER BY clause.
"""

# Syntax:
"""
The basic syntax of GROUP BY clause is given below. The GROUP BY clause must follow
the conditions in the WHERE clause and must precede the ORDER BY clause if one is
used.
________________________________________________________________________________
SELECT column-list
FROM table_name
WHERE [ conditions ]
GROUP BY column1, column2 .... columnN
________________________________________________________________________________

You can use more than one column in the GROUP BY clause. Make sure whatever column
you are using to group, that column should be available in column-list.
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

If you want to know the total amount of salary on each customer, then GROUP BY
query would be as follows:
________________________________________________________________________________
sqlite> SELECT NAME, SUM(SALARY) FROM COMPANY GROUP BY NAME;
________________________________________________________________________________

This would produce following result:
________________________________________________________________________________
Name        SALARY
----------  -----------
Allen       15000.0
David       85000.0
James       10000.0
Kim         45000.0
Mark        65000.0
Paul        20000.0
Teddy       20000.0
________________________________________________________________________________

Now, let us create three more records in COMPANY table using the following INSERT
statements:
________________________________________________________________________________
INSERT INTO COMPANY VALUES (8, 'Paul', 24, 'Houston', 20000.00 );
INSERT INTO COMPANY VALUES (9, 'James', 44, 'Norway', 5000.00 );
INSERT INTO COMPANY VALUES (10, 'James', 45, 'Texas', 5000.00 );
________________________________________________________________________________

Now, our table has the following records with duplicate names:
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
8       Paul        24      Houston         20000.0
9       James       44      Norway          5000.0
10      James       45      Texas           5000.0
________________________________________________________________________________

Again, let us use the same statement to group-by all the records using NAME column
as follows:
________________________________________________________________________________
sqlite> SELECT NAME, SUM(SALARY) FROM COMPANY GROUP BY NAME ORDER BY NAME;
________________________________________________________________________________

This would produce the following result:
________________________________________________________________________________
Name        SALARY
----------  -----------
Allen       15000.0
David       85000.0
James       20000.0
Kim         45000.0
Mark        65000.0
Paul        40000.0
Teddy       20000.0
________________________________________________________________________________

Let us use ORDER BY clause along with GROUP BY clause as follows:
________________________________________________________________________________
sqlite> SELECT NAME, SUM(SALARY) FROM COMPANY GROUP BY NAME ORDER BY NAME DESC;
________________________________________________________________________________

This would produce the following result:
________________________________________________________________________________
Name        SALARY
----------  -----------
Teddy       20000.0
Paul        40000.0
Mark        65000.0
Kim         45000.0
James       20000.0
David       85000.0
Allen       15000.0
________________________________________________________________________________
