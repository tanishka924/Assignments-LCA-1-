# List operations
my_list = [10, 20, 30, 40]

print("Original List:", my_list)

my_list.append(50)
print("After append:", my_list)

my_list.insert(1, 15)
print("After insert:", my_list)

my_list.remove(20)
print("After remove:", my_list)

# Tuple operations
my_tuple = (10, 20, 30, 20)

print("\nOriginal Tuple:", my_tuple)
print("Count of 20:", my_tuple.count(20))
print("Index of 30:", my_tuple.index(30))

# Dictionary operations
student = {
    "name": "Tanishka",
    "age": 18,
    "branch": "AI & DS"
}

print("\nOriginal Dictionary:", student)
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())
print("Name:", student.get("name"))

student.pop("age")
print("After pop:", student)
