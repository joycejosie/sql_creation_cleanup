import sqlite3
from emp import Employee

connection = sqlite3.connect('employee.db')

c = connection.cursor()

#c.execute("INSERT INTO employees VALUES ('Luigi', 'Lafontant', 2000)")

emp_1 = Employee('John', 'Doe', 9000)
emp_2 = Employee('Jane', 'Doe', 80000)


c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", 
    {'first':emp_1.first, 'last': emp_1.last, 'pay': emp_1.pay})

connection.commit()

c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", 
    {'first':emp_2.first, 'last': emp_2.last, 'pay': emp_2.pay})

connection.commit()

connection.close()