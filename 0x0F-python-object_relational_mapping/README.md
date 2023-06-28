1. The MySQLdb is a DB-API module that integrates MySQL into our Python scripts.

2. The SQLAlchemy Object Relational Mapper presents a method of associating user-defined python classes with database tables, and instances of those classes(objects) with rows in their corresponding tables.

How to craete tables, insert and select using Python MySQL:

import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "root",
    database = "testdatabase"
    )

mycursor = db.cursor()

"""To craete a table"""

mycursor.execute("CREATE TABLE Person (name VARCHAR(50), age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INREAMENT)")

"""Inserting into our table"""
mycursor.execute("INSERT INTO Person (name, age) VALUES (%s,%s)", ("Tim", 20))
db.commit()

"""To get all rows and columns inside our database"""
mycursor.execute("SELECT * FROM Person")

for x in mycursor:
    print(x)

3. With an ORM, dvelopers can interact with the database using objects and their methods, rather than writing raw SQL queries.
