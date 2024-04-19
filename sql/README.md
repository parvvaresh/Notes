# SQL Tutorial
SQL is a standard language for storing, manipulating and retrieving data in databases.

Our SQL tutorial will teach you how to use SQL in: MySQL, SQL Server, MS Access, Oracle, Sybase, Informix, Postgres, and other database systems.


- this repo update daily for **amirkabir university**


# Table of Contents

- intro + 
 
- select +

- distinct +

- where + 

- order by +

- and + 

- or + 

- not +

- insert into + 

- null value + 

- update + 

- delete + 

- limit +

- count 

- sum

- avg

- like

- wildcards

- in

- between

- as





# intro
SQL is a standard language for accessing and manipulating databases.

## What is SQL?
1.  SQL stands for Structured Query Language
2.  SQL lets you access and manipulate databases
3.  SQL became a standard of the American National       Standards Institute (ANSI) in 1986, and of the International Organization for Standardization (ISO) in 1987

## What Can SQL do?

1.  SQL can execute queries against a database
2.  SQL can retrieve data from a database
3.  SQL can insert records in a database
4.  SQL can update records in a database
5.  SQL can delete records from a database
6.  SQL can create new databases
7.  SQL can create new tables in a database
8.  SQL can create stored procedures in a database
9.  SQL can create views in a database
10. SQL can set permissions on tables, procedures, and views


# SELECT

The **SELECT** statement is used to select data from a database.


## Example 

All customer numbers and city in the customer table :‌ 

```sql
SELECT CustomerName, City FROM Customers;
```

## Syntax :

```sql
SELECT column1, column2, ... 
FROM tabel_name;
```

**NOTE:** Here, column1, column2, ... are the field names of the table you want to select data from.

The table_name represents the name of the table you want to select data from. 


## Select ALL columns 

If you want to return all columns, without specifying every column name, you can use the SELECT * syntax:



```sql
SELECT * FROM Customers;
```


# SELECT DISTINCT

The **SELECT DISTINCT** statement is used to return only distinct (different) values.


## Example 
Select all the different countries from the "Customers" table:

```sql
SELECT DISTINCT country FROM Customers;
```

Inside a table, a column often contains many duplicate values; and sometimes you only want to list the different (distinct) values.

## Syntax 

```sql
SELECT DISTINCT column1 , column2 , ...
FROM table_name
```

## Count Distinct
By using the DISTINCT keyword in a function called COUNT, we can return the number of different countries.



```sql
SELECT COUNT(DISTINCT Country) FROM Customers;
```

# WHERE

The **WHERE** clause is used to filter records.

It is used to extract only those records that fulfill a specified condition.

## Example
Select all customers from Mexico:

```sql
SELECT * FROM Customers WHERE Country='Mexico';
```

## Syntax

```sql
SELECT column1 , column2, column3, ...
FROM table_name 
WHERE condition;
```

**Note:** The WHERE clause is not only used in SELECT statements, it is also used in UPDATE, DELETE, etc.!

## Text Fields vs. Numeric Fields

SQL requires single quotes around text values (most database systems will also allow double quotes).

However, numeric fields should not be enclosed in quotes:

```sql
SELECT * FROM Customers WHERE Customer_id=1;
```
## The following operators can be used in the WHERE clause:

| Operator | Description |
|---|---|
| = | Equal |
| > | Greater than |
| < | Less than |
| >= | Greater than or equal |
| <= | Less than or equal |
| != | Not equal. Note: In some versions of SQL this operator may be written as <> |
| BETWEEN | Between a certain range |
| LIKE | Search for a pattern |
| IN | To specify multiple possible values for a column |

# Order by
The ORDER BY keyword is used to sort the result-set in ascending or descending order.

## Syntax
```sql
SELECT column1, column2, ...
FROM tabel_neme
ORDER BY column1, column2, ... ASC|DESC;
```

**NOTE 1:** The ORDER BY keyword sorts the records in ascending order by default. To sort the records in descending order, use the DESC keyword


**NOTE 2:** The following SQL statement selects all customers from the "Customers" table, sorted by the "Country" and the "CustomerName" column. This means that it orders by Country, but if some rows have the same Country, it orders them by CustomerName:

```sql
SELECT * FROM Customers
ORDER BY Country, CustomerName;
```

**NOTE 3:**The following SQL statement selects all customers from the "Customers" table, sorted ascending by the "Country" and descending by the "CustomerName" column:

```sql
SELECT * FROM Customers
ORDER BY Country ASC, CustomerName DESC;
```
 


## Example
sort the products by price: 


```sql
SELECT * FROM products ORDER BY Price;
```



# AND

The `WHERE` clause can contain one or many `AND` operators.



The `AND` operator displays a record if all the conditions are TRUE.


## Syntax

```sql
SELECT column1, column2, ...
FROM tabel_name
WHERE condition1 AND condition2 AND condition3 ...;
```
## Example

The following SQL statement selects all fields from Customers where Country is "Germany" AND City is "Berlin" AND PostalCode is higher than 12000:

```SQL
SELECT * FROM Customers
WHERE Country = 'Germany'
AND
City = 'Berlin'
AND
PostalCode > 1200;
```


# OR

The WHERE clause can contain one or more OR operators.

The OR operator displays a record if any of the conditions are TRUE.

## Syntax


```sql
SELECT column1, column2, ...
FROM tabel_name
WHERE condition1 AND condition2
```
## Example

The following SQL statement selects all fields from Customers where either City is "Berlin", CustomerName starts with the letter "G" or Country is "Norway":


```sql
SELECT * FROM Customers
WHERE City = 'Berlin' 
OR
CustomerName LIKE 'G%'
OR
Country = 'Norway';
```

# NOT

The NOT operator is used in combination with other operators to give the opposite result, also called the negative result.

## Syntax

```sql
SELECT column1, column2, ...
FROM table_name
WHERE NOT condition;
```

## Example

Select only the customers that are NOT from Spain:


```sql
SELECT * 
FROM Customers
WHERE NOT Country = 'Spain';
```
# INSERT INTO

The INSERT INTO statement is used to insert new records in a table.

## Syntax

1.  Specify both the column names and the values to be inserted:

    ```sql
    INSERT INTO table_name (column1, column2, column3, ...)
    VALUES (value1, value2, value3, ...);
    ```

2.  If you are adding values for all the columns of the table, you do not need to specify the column names in the SQL query. However, make sure the order of the values is in the same order as the columns in the table. Here, the INSERT INTO syntax would be as follows:

```sql
INSERT INTO table_name
VALUES (value1, value2, value3, ...);
```



## Example

1. The following SQL statement inserts a new record in the "Customers" table:


    ```sql
    INSERT INTO Customers (CustomerName, ContactName, Address, City, PostalCode, Country)
    VALUES ('Cardinal', 'Tom B. Erichsen', 'Skagen 21', 'Stavanger', '4006', 'Norway')
    ```


2. Insert Data Only in Specified Columns

    It is also possible to only insert data in specific columns.

    The following SQL statement will insert a new record, but only insert data in the "CustomerName", "City", and "Country" columns (CustomerID will be updated automatically):


    ```sql
    INSERT INTO Customers (CustomerName, City, Country)
    VALUES ('Cardinal', 'Stavanger', 'Norway');
    ```
3. Insert Multiple Rows
It is also possible to insert multiple rows in one statement.

    To insert multiple rows of data, we use the same INSERT INTO statement, but with multiple values:

    ```sql
    INSERT INTO Customers (CustomerName, ContactName, Address, City, PostalCode, Country)
    VALUES
    ('Cardinal', 'Tom B. Erichsen', 'Skagen 21', 'Stavanger', '4006', 'Norway'),
    ('Greasy Burger', 'Per Olsen', 'Gateveien 15', 'Sandnes', '4306', 'Norway'),
    ('Tasty Tee', 'Finn Egan', 'Streetroad 19B', 'Liverpool', 'L1 0AA', 'UK');
    ```


**NOTE :** without adding a value to this field. Then, the field will be saved with a NULL value.



# NULL Values

A field with a NULL value is a field with no value.


How to Test for NULL Values?

##  Syntax

1. IS NULL Syntax

    ```sql
    SELECT column_names
    FROM table_name
    WHERE column_name  IS NULL
    ````

2. IS NOT NULL Syntax

    ```sql
    SELECT column_names
    FROM table_name
    WHERE column_name  IS NOT NULL
    ````
## Example

The following SQL lists all customers with a NULL value in the "Address" field:

```sql
SELECT *
FROM Customer 
WHERE Address IS NULL
```
The following SQL lists all customers with a value in the "Address" field:


```sql
SELECT *
FROM Customer 
WHERE Address IS NOT NULL
```

# UPDATE
The UPDATE statement is used to modify the existing records in a table.

## Syntax

```sql
UPDATE table_name
SET column1 = value1, column2 = value2, ...

WHERE condition;
```

## Example

The following SQL statement updates the first customer (CustomerID = 1) with a new contact person and a new city.


```sql
UPDATE customer
SET ContactName = 'Alfred', City = 'tehran'
WHERE CustomerID = 1;
```

yeah i love tehran


**NOTE:** Be careful when updating records. If you omit the WHERE clause, ALL records will be updated!

# DELETE

The DELETE statement is used to delete existing records in a table.


## Syntax

```sql
DELETE FROM table_name WHERE condition;
```

## Example

The following SQL statement deletes the customer "Alfreds Futterkiste" from the "Customers" table:

```sql
DELETE FROM Customer WHERE CustomerName = 'Alfreds Futterkiste';
```

## - Delete All Records


```sql
DELETE FROM table_name;
```

## - Delete a Table

```sql
DROP TABLE table_name;
```

# LIMIT

The `LIMIT` clause is used to specify the number of records to return.

## Syntax

```sql
SELECT column_name(s)
FROM table_name
WHERE condition
LIMIT number;
```

## Example

The following SQL statement shows the equivalent example for MySQL:

```sql
SELECT * 
FROM Costumer 
LIMIT 3;
```