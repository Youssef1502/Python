#!/usr/bin/python3

'''================================================================================
--    Author    :   			YOUSSEF ADEL YOUSSEF

-- Description  :   Python code that manage a database for employees.
================================================================================'''

import sqlite3

# Connect to SQLite database (it will create the database if it doesn't exist)
conn = sqlite3.connect('employee.db')
cursor = conn.cursor()

# Create the employee table
cursor.execute('''
CREATE TABLE IF NOT EXISTS employee (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    job TEXT NOT NULL,
    salary REAL NOT NULL
)
''')
conn.commit()

def add_employee(name, job, salary, emp_id=None):
    if emp_id is not None:
        cursor.execute('INSERT INTO employee (id, name, job, salary) VALUES (?, ?, ?, ?)', (emp_id, name, job, salary))
    else:
        cursor.execute('INSERT INTO employee (name, job, salary) VALUES (?, ?, ?)', (name, job, salary))
    conn.commit()
    print("Employee added successfully.")

def print_employee_data():
    cursor.execute('SELECT * FROM employee')
    rows = cursor.fetchall()
    if rows:
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Job: {row[2]}, Salary: {row[3]}")
    else:
        print("There are no employees in the database.")

def remove_employee(emp_id):
    cursor.execute('SELECT * FROM employee WHERE id = ?', (emp_id,))
    row = cursor.fetchone()
    if row:
        cursor.execute('DELETE FROM employee WHERE id = ?', (emp_id,))
        conn.commit()
        print("Employee removed successfully.")
    else:
        print(f"No employee found with ID {emp_id}.")

def edit_employee(emp_id, name=None, job=None, salary=None):
    cursor.execute('SELECT * FROM employee WHERE id = ?', (emp_id,))
    row = cursor.fetchone()
    if row:
        if name:
            cursor.execute('UPDATE employee SET name = ? WHERE id = ?', (name, emp_id))
        if job:
            cursor.execute('UPDATE employee SET job = ? WHERE id = ?', (job, emp_id))
        if salary:
            cursor.execute('UPDATE employee SET salary = ? WHERE id = ?', (salary, emp_id))
        conn.commit()
        print("Employee data updated successfully.")
    else:
        print(f"No employee found with ID {emp_id}.")
        return False  # Indicate that the ID was invalid
    return True  # Indicate that the update was successful

def get_valid_salary(prompt):
    while True:
        try:
            salary = float(input(prompt))
            return salary
        except ValueError:
            print("Invalid input. Please enter a valid number for the salary.")

def main():
    while True:
        print("1- Add new employee")
        print("2- Print employee data")
        print("3- Remove employee from the system")
        print("4- Edit employee information")
        print("5- Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter employee name: ")
            job = input("Enter employee job: ")
            salary = get_valid_salary("Enter employee salary: ")
            add_employee(name, job, salary)
        elif choice == '2':
            print_employee_data()
        elif choice == '3':
            emp_id = int(input("Enter employee ID to remove: "))
            remove_employee(emp_id)
        elif choice == '4':
            while True:
                emp_id_input = input("Enter employee ID to edit: ")
                try:
                    emp_id = int(emp_id_input)
                except ValueError:
                    print("Invalid input. Please enter a numeric employee ID.")
                    continue

                valid_id = cursor.execute('SELECT 1 FROM employee WHERE id = ?', (emp_id,)).fetchone()
                if not valid_id:
                    print(f"No employee found with ID {emp_id}. Please enter a valid ID.")
                else:
                    break

            print("Leave the field empty if you do not want to change it.")
            name = input("Enter new name (or press Enter to skip): ")
            job = input("Enter new job (or press Enter to skip): ")
            salary_input = input("Enter new salary (or press Enter to skip): ")
            salary = float(salary_input) if salary_input else None
            name = name if name else None
            job = job if job else None
            edit_employee(emp_id, name, job, salary)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()

# Close the database connection
conn.close()
