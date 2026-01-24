student = {
    "name": "John",
    "age": 28,
    "height": 70,
    "weight": 90,
    "eye_color": "blue"
}

print("Original Dictionary:", student)

# clear method
student_copy = student.copy()
student_copy.clear()
print("n clear",student_copy)

# copy
copy_dist = student.copy()
print("copy is here", copy_dist)

# fromkeys
keys = ["id","marks", "grade"]
dist_keys = dict.fromkeys(keys, 0)
print(dist_keys)

# get method
print("student name", student.get("name"))
print("student address", student.get("address", "not found"))

# items
print("all items", student.items())

# Keys
print("here is keys",student.keys())

# values
print("values", student.values())

# pop
age = student.pop("age")
print("\npop('age'):", age)
print("After pop:", student)

# 9. dict.popitem()
item = student.popitem()
print("\npopitem():", item)
print("After popitem:", student)

# setDefault
student.setdefault("city" , "Lahore")
print("setDefault", student)

# update
student.update({"age": 21 , "city": "New York"})
print("update", student)
