# Lists ===============================
student_names = ["Homer", "Mark"]

for name in student_names:
    print("Student name is {0}".format(name))

# List comprehension

# Dictionaries ========================
students = {1: "Homer", 2: "Mark"}

for name in students:
    print("Student {0} name is {1}".format(name, students[name]))

# Exceptions ==========================
student = {
    "name": "Mark",
    "id": 15103,
    "feedback": None
}

try:
    last_name = student["last_name"]
except KeyError:
    print("Key not found!")

# Other data types ===================
my_set = {1, 2, 1, 3, 5}

print(my_set)
