# team3_sql_database_cleanup
 sql and pyton code for redundancies 

***Before we start:***

- Since there is no  default libaray, install a third-party Python SQL driver to interact w/ PostgreSQL.
- Python SQL driver: **psycopg2** <sub>(install through pip)</sub>
- Import the driver than create the manditory function "create_connection() to access your database.
- Follow this article for more instructions
    - https://realpython.com/python-sql-libraries/#postgresql
    - https://www.postgresqltutorial.com/postgresql-python/connect/
- Instead of creating a new one we will just connect to the default database **dvdrental**

***11/19/20 Update***

- Several complications occured with installing the PostgreSQL driver
- Using SQLite will be a method I'll be using from now for this script
- By default, your Python installation contains a Python SQL library named sqlite3 that you can use to interact with an SQLite database