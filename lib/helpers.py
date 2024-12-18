from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()

# We'll implement the department functions in this lesson

def list_departments():
    departments = Department.get_all()
    for department in departments:
        print(department)


def find_department_by_name():
    name = input("Enter the department's name: ")
    department = Department.find_by_name(name)
    print(department) if department else print(
        f'Department {name} not found')


def find_department_by_id():
    #use a trailing underscore not to override the built-in id function
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    print(department) if department else print(f'Department {id_} not found')


def create_department():
    name = input("Enter the department's name: ")
    location = input("Enter the department's location: ")
    try:
        department = Department.create(name, location)
        print(f'Success: {department}')
    except Exception as exc:
        print("Error creating department: ", exc)


def update_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        try:
            name = input("Enter the department's new name: ")
            department.name = name
            location = input("Enter the department's new location: ")
            department.location = location

            department.update()
            print(f'Success: {department}')
        except Exception as exc:
            print("Error updating department: ", exc)
    else:
        print(f'Department {id_} not found')


def delete_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        department.delete()
        print(f'Department {id_} deleted')
    else:
        print(f'Department {id_} not found')


# You'll implement the employee functions in the lab

def list_employees():
    employees = Employee.get_all()
    for employee in employees:
        print(employee)


def find_employee_by_name():
    name = input("Enter the employee's name: ")
    employee = Employee.find_by_name(name)
    print(employee) if employee else print(f'Employee {name} not found')


def find_employee_by_id():
    employee_id = int(input("Enter the employee's ID: "))
    employee = Employee.find_by_id(employee_id)
    print(employee) if employee else print(f'Employee with ID {employee_id} not found')

def create_employee():
    name = input("Enter the employee's name: ")
    job_title = input("Enter the employee's job title: ")
    department = input("Enter the employee's department: ")
    building = input("Enter the employee's building: ")
    floor = input("Enter the employee's floor: ")

    employee = Employee(name, job_title, department, building, floor)
    employee.save()
    print("Employee created successfully!")

    


def update_employee():
    employee_id = int(input("Enter the employee's ID: "))
    employee = Employee.find_by_id(employee_id)
    if employee:
        print("Current employee details:")
        print(employee)
        
        name = input("Enter new name (press Enter to skip): ")
        job_title = input("Enter new job title (press Enter to skip): ")
        department = input("Enter new department (press Enter to skip): ")
        building = input("Enter new building (press Enter to skip): ")
        floor = input("Enter new floor (press Enter to skip): ")

        if name:
            employee.name = name
        if job_title:
            employee.job_title = job_title
        if department:
            employee.department = department
        if building:
            employee.building = building
        if floor:
            employee.floor = floor

        employee.save()
        print("Employee updated successfully!")
    else:
        print(f'Employee with ID {employee_id} not found')


def delete_employee():
    employee_id = int(input("Enter the employee's ID: "))
    employee = Employee.find_by_id(employee_id)
    if employee:
        confirm = input(f"Are you sure you want to delete {employee.name}? (yes/no): ")
        if confirm.lower() == "yes":
            employee.delete()
            print(f"Employee {employee.name} deleted successfully!")
        else:
            print("Deletion cancelled.")
    else:
        print(f'Employee with ID {employee_id} not found')

def list_department_employees():
    department_id = input("Enter the department's ID: ")
    department = Department.find_by_id(department_id)
    if department:
        employees = department.employees()
        if employees:
            print(f"Employees in {department.name}:")
            for employee in employees:
                print(employee)
        else:
            print(f"No employees found in {department.name}")
    else:
        print(f'Department with ID {department_id} not found')
