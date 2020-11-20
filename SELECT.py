import sqlite3

connection = sqlite3.connect('employee.db')

c = connection.cursor()

#c.execute("SELECT * FROM employees WHERE last='Lafontant'")

c.execute("SELECT * FROM employees WHERE last=:last", {'last': 'Lafontant'})

print(c.fetchall())

c.execute("SELECT * FROM employees WHERE last=:last", {'last': 'Doe'})

print(c.fetchall())

# c.fetchone()
# c.fetchmany(5)
# c.fetchall()



connection.commit()
connection.close()