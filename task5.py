class Employee:
    def __init__(Nacar, name, position, salary):
        Nacar.name = name
        Nacar.position = position
        Nacar.salary = salary

    def give_raise(Nacar, amount):
        Nacar.salary += amount
        print(f"Salary increased by: ${amount}")

    def display_employee(Nacar):
        print(f"Employee Name: {Nacar.name}")
        print(f"Position: {Nacar.position}")
        print(f"Salary: ${Nacar.salary}")

employee = Employee("Nacar,joana Rose M.", "designer", 60000)

employee.give_raise(5000)

employee.display_employee()
