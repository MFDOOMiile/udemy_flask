#Destructing Variables
t = 5, 11
x, y = t

print(x, y)

###~~~~~###

student_attendance = {"Rafi": 96, "Nick": 61, "Adam": 87}

print(list(student_attendance.items()))

for t in student_attendance.items():
    print(t)
    #print(f"{student}: {attendance}")

###~~~~~###

people = [("Bob", 42, "Mechanic"), ("James", 24, "Artist"), ("Harry", 32, "Lecturer")]

for name, age, profession in people: 
    print(f"Name: {name}, Age: {age}, Profession: {profession}")

###~~~~~###

person = ("Bob", 42, "Mechanic")
name, _, profession = person    # _ is used to ignore a value

print(name, profession)

###~~~~~###

head, *tail = [1, 2, 3, 4, 5]
print(head)
print(tail)

*head, tail = [1, 2, 3, 4, 5]
print(head)
print(tail)