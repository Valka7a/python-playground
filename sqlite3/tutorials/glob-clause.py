"""
The SQLite GLOB operator is used to match only text values against a pattern using
wildcards. If the search expression can be matched to the pattern expression, the
GLOB operator will return true, which is 1. Unlike LIKE operator, GLOB is case
sensitive and it follows syntax of UNIX for specifying THE following wildcards.
Sensitive at lower and uppercase.

    * The asterisk sign(*)
    * The question mark(?)

The asterisk sign represents zero or multiple numbers or characters. The ? represents
a single number or character.
"""

# Syntax:
"""
The basic syntax of * and ? is as follows:
________________________________________________________________________________
SELECT FROM table_name
WHERE column GLOB 'XXXX*'

or

SELECT FROM table_name
WHERE column GLOB '*XXXX*'

or

SELECT FROM table_name
WHERE column GLOB 'XXXX?'

or

SELECT FROM table_name
WHERE column GLOB '?XXXX'

or

SELECT FROM table_name
WHERE column GLOB '?XXXX?'

or

SELECT FROM table_name
WHERE column GLOB '????'
________________________________________________________________________________

You can combine N number of conditions using AND or OR operators. Here XXXX could be
any numberic or string value.
"""

# Example:
"""
Here are number of examples showing WHERE part having different LIKE clause with
'*' and '?' operators:
_________________________________________________________________________________
| Statement                 | Description                                       |
================================================================================|
| WHERE SALARY GLOB '200%'  | Finds any values that start with 200              |
| WHERE SALARY LIKE '%200%' | Finds any values that have 200 in any position    |
| WHERE SALARY LIKE '?00*'  | Finds any values that have 00 in the second and   |
|                           | third position                                    |
| WHERE SALARY LIKE '2??'   | Finds any values that start with 2 and are at     |
|                           | least 3 characters in length                      |
| WHERE SALARY LIKE '*2'    | Finds any values that end with 2                  |
| WHERE SALARY LIKE '?2*3'  | Finds any values that have a 2 in the second      |
|                           | position and end with a 3                         |
| WHERE SALARY LIKE '2???3' | Finds any values in a five-digit number that      |
|                           | start with 2 and end with 3                       |
---------------------------------------------------------------------------------

Let us take a real example, consider COMPANY table is having the following records:
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

Following is an example, which would display all the records from COMPANY table
where AGE starts with 2:
________________________________________________________________________________
sqlite> SELECT * FROM COMPANY WHERE AGE  GLOB '2*';
________________________________________________________________________________

This would produce the following result:
________________________________________________________________________________
ID      Name        Age     ADDRESS         SALARY
-----   ----------  ------  ------------    -----------
2       Allen       25      Texas           15000.0
3       Teddy       23      Norway          20000.0
4       Mark        25      Rich-Mond       65000.0
5       David       27      Texas           85000.0
6       Kim         22      South-Hall      45000.0
7       James       24      Houston         10000.0
________________________________________________________________________________

Following is and example, which sould display all the records from COMPANY table
where ADDRESS will have a hyphen (-) inside the text:
________________________________________________________________________________
sqlite> SELECT * FROM COMPANY WHERE ADDRESS  GLOB '*-*';
________________________________________________________________________________

This would produce the following result:
________________________________________________________________________________
ID      Name        Age     ADDRESS         SALARY
-----   ----------  ------  ------------    -----------
4       Mark        25      Rich-Mond       65000.0
6       Kim         22      South-Hall      45000.0
________________________________________________________________________________
