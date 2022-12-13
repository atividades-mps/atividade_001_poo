# Creating a class Employee with 3 attributes: name, rg, cpf
class Employee: 
    def __init__(self, name: str, rg: str, cpf: str):
        self.name = name
        self.rg = rg
        self.cpf = cpf
    
    def work(self):
        print(f"{self.name} is working...")

# Creating two diferent objects
employee_1 = Employee("Jorge", "1111111-1", "111.111.111-11")
employee_2 = Employee("Marcelo", "2222222-2", "222.222.222-22")

employee_1.work() # output: "Jorge is working..."
employee_2.work() # output: "Marcelo is working..."

# Two diferent ids
print(id(employee_1))
print(id(employee_2))

# But...
employee_1 = employee_2
employee_2.name = "The impostor"

# Results in two equal outputs
employee_1.work() # output: "The impostor is working..."
employee_2.work() # output: "The impostor is working..."

# Two equal ids
print(id(employee_1))
print(id(employee_2))