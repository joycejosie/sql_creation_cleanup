import sqlite3

connection = sqlite3.connect('employee.db')

c = connection.cursor()

c.execute("""CREATE TABLE employees (
    first text,
    last text,
    pay integer
    )""")

def insert_emp(emp):
    with connection:
        c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", 
            {'first':emp.first, 'last': emp.last, 'pay': emp.pay})

def get_emps_by_name(lastname):
    c.execute("SELECT * FROM employees WHERE last=:last", {'last': 'Lafontant'})
    return c.fetchall()

de


connection.commit()
connection.close()