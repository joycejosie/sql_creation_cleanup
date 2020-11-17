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