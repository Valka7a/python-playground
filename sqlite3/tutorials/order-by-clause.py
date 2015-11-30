"""
The SQLite ORDER BY clause is used to sort the data in ascending or descending
order, based on one or more columns.
"""

# Syntax:
"""
The basic syntax of ORDER BY clause is as follows:
________________________________________________________________________________
SELECT column-list
FROM table_name
[WHERE condition]
[ORDER BY column1, column2, .. columnN] [ASC | DESC];
________________________________________________________________________________

You can use more than one column in the ORDER BY clause. Make sure whatever column
you are using to sort, that column should be available in column-list.
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

Following is and example, which would sort the result in descending order by SALARY:
________________________________________________________________________________
sqlite> SELECT * FROM COMPANY ORDER BY SALARY ASC;
________________________________________________________________________________

This would produce the following result:
________________________________________________________________________________
ID      Name        Age     ADDRESS         SALARY
-----   ----------  ------  ------------    -----------
7       James       24      Houston         10000.0
2       Allen       25      Texas           15000.0
1       Paul        32      California      20000.0
3       Teddy       23      Norway          20000.0
6       Kim         22      South-Hall      45000.0
4       Mark        25      Rich-Mond       65000.0
5       David       27      Texas           85000.0
________________________________________________________________________________

Following is an example, which would sort the result in descending order by NAME
and SALARY:
________________________________________________________________________________
sqlite> SELECT * FROM COMPANY ORDER BY NAME, SALARY ASC;
________________________________________________________________________________

This would produce the following result:
________________________________________________________________________________
ID      Name        Age     ADDRESS         SALARY
-----   ----------  ------  ------------    -----------
2       Allen       25      Texas           15000.0
5       David       27      Texas           85000.0
7       James       24      Houston         10000.0
6       Kim         22      South-Hall      45000.0
4       Mark        25      Rich-Mond       65000.0
1       Paul        32      California      20000.0
3       Teddy       23      Norway          20000.0
________________________________________________________________________________

Following is an example, which would sort the result in descending order by NAME:
________________________________________________________________________________
sqlite> SELECT * FROM COMPANY ORDER BY NAME DESC;
________________________________________________________________________________

This would produce the following result:
________________________________________________________________________________
ID      Name        Age     ADDRESS         SALARY
-----   ----------  ------  ------------    -----------
3       Teddy       23      Norway          20000.0
1       Paul        32      California      20000.0
4       Mark        25      Rich-Mond       65000.0
6       Kim         22      South-Hall      45000.0
7       James       24      Houston         10000.0
5       David       27      Texas           85000.0
2       Allen       25      Texas           15000.0
________________________________________________________________________________
