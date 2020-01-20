###~~~Object_Oriented Programming~~~###
student = {"name": "Rafi", "grades": (89, 90, 93, 78, 90)}

def average(sequence):
    return sum(sequence) / len(sequence)

print(average(student["grades"]))           #method one without O.O.P

###~~~###

class Student:
    def __init__(self):         #init is a method, not a function
        self.name = "Rafi"
        self.grades = (90, 93, 90, 78, 90)

    def average_grades(self):
        return sum(self.grades) / len(self.grades)

student = Student()
print(student.name)
print(student.grades)
print(Student.average_grades(student))
print(student.average_grades())

###~~~###

class Student: 
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average_grades(self):
        return sum(self.grades) / len(self.grades)

student = Student("Rafiki", (100, 100, 94, 88, 91))
student2 = Student("Rafa", (100, 71, 94, 92, 90))

print(student.name)
print(student.average_grades())
print(student2.name)
print(student2.average_grades())


(self, name)
self.name
self.items = []

(self, name, price)
item = {'name': name, 'price': price}
self.items.append(item)

return sum([item['price'] for item in self.items])