class Person:
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

    def describe(self):
        return f"{self.name} is a {self.sex} and {self.age} years of old"

maria = Person("Maria",23,"female")
print(Person.describe(maria))
