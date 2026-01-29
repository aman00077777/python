student = {
    "name": "Alice",
    "age": 21,
    "courses": ["Math", "Science", "Art"],
    "is_enrolled": True
}

print(type(student))  

print(student)
print(student["name"])
print(student["courses"][1])
student["age"] = 22
student["grade"] = "A"
print(student)
student.pop("is_enrolled")
print(student)