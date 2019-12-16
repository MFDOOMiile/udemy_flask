#Dictionaries 
friend_ages = {"Rolf": 24, "Adam": 30, "Anne": 27}

friend_ages["Rafi"] = 32        #add to dictionary
friend_ages["Rolf"] = 25        #change entry in dictionary

print(friend_ages["Adam"])      #print only one entry
print(friend_ages)              #printing dictionary

###~~~~~~###

friends = [
    {"name": "Rafi", "age": 32},
    {"name": "Nick", "age": 29},
    {"name": "Adam", "age": 24}
]

print(friends[1])
print(friends[0]["name"])

###~~~~~###

student_attendance = {"Rafi": 96, "Nick": 61, "Adam": 87}

for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")

###~~~~~###

student_attendance = {"Rafi": 96, "Nick": 61, "Adam": 87}

if "Rafi" in student_attendance:
    print(f"Rafi: {student_attendance['Rafi']}")
else:
    print("Rafi is not a student in this class.")

###~~~~~###

student_attendance = {"Rafi": 96, "Nick": 61, "Adam": 87}

attendance_values = student_attendance.values()
print(sum(attendance_values) / len(attendance_values))