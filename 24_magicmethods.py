###~~~Magic Methods: __str__ and __repr__~~~###
class Person: 
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):          #__str__ is for turning objects into strings
        return f"Person: {self.name}, {self.age} years old."

    def __repr__(self):
        return f"<Person('{self.name}', {self.age})>"

rafi = Person("Rafi", 32)
print(rafi)