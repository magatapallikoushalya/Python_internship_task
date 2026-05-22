
student1 = {
    "roll_no": 101,
    "name": "Kaushalya",
    "course": "Python"
}

student2 = {
    "roll_no": 102,
    "name": "Rahul",
    "course": "Java"
}

student3 = student1

print("Student 1 Details:", student1)
print("Student 2 Details:", student2)
print("Student 3 Details:", student3)

print("\nChecking Identity Operators\n")

print("student1 is student2:", student1 is student2)

print("student1 is not student2:", student1 is not student2)

print("student1 is student3:", student1 is student3)

print("student1 is not student3:", student1 is not student3)
