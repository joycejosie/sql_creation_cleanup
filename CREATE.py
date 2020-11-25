import sqlite3
from emp import Employee


connection = sqlite3.connect (':memory:')

cursor = connection.cursor()

cursor.execute("""CREATE TABLE employees (
    first text,
    last text,
    pay integer
    )""")

def insert_emp(emp):
    with connection:
        cursor.execute("INSERT INTO employees VALUES (:first, :last, :pay)", 
            {'first':emp.first, 'last': emp.last, 'pay': emp.pay})

def get_emps_by_name(lastname):
    cursor.execute("SELECT * FROM employees WHERE last = :last", {'last': lastname})
    return cursor.fetchall()

def update_pay(emp, pay):
    with connection:
        cursor.execute("""UPDATE employees SET pay = :pay
                    WHERE first = :first AND last = :last""",
                    {'first': emp.first, 'last': emp.last, 'pay': emp.pay})



def remove_emp(emp):
    with connection:
        cursor.execute("DELETE from employees WHERE first = :first AND last = :last",
                    {'first': emp.first, 'last': emp.last})


emp_1 = Employee('Joyce', 'Lafontant', 48080)
emp_2 = Employee('Carl', 'Morcy', 35477)
emp_3 = Employee('Moussa', 'Fomba', 98743)
emp_4 = Employee('Urji', 'Haji', 80000)
emp_5 = Employee('Brodrick', 'Stanley', 73736)
emp_6 = Employee('Jamie', 'Edward', 191929)
emp_7 = Employee('John', 'Doe', 9000)
emp_8 = Employee('Jane', 'Doe', 80000)



insert_emp(emp_1)
insert_emp(emp_2)
# insert_emp(emp_3)
# insert_emp(emp_4)
# insert_emp(emp_5)
# insert_emp(emp_6)
# insert_emp(emp_7)
# insert_emp(emp_8)

show = get_emps_by_name('Lafontant')
print(show)

update_pay(emp_1, 95000)


show = get_emps_by_name('Lafontant')
print(show)



# show3 = remove_emp(emp_1)
# print(show3)





connection.close()