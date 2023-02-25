class Person:
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

    def describe(self):
        return f"{self.name} is a {self.sex} and {self.age} years of old"

class Man(Person):

    def __init__(self,name,age):
        self.sex = 'Male'
        self.name = name
        self.age = age

joao = Man('Joao',30)
print(joao.describe())
