class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
def get_salary_info(self):
        return "Заробітна плата " + self.name + ": " + str(self.salary)
emp1 = Employee("Олександр", "Менеджер", 25000)
print(emp1.get_salary_info())