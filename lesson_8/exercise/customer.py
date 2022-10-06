class Customer:
    def __init__(self, name, cpf, age):
        self.name = name
        self.cpf = cpf
        self.age = age
        
    def __str__(self):
        return "Name: " + self.name + "\nCPF: " + str(self.cpf) + "\nAge: " + str(self.age)   
        