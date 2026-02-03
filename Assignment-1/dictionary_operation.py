# Program to demonstrate Dictionary Operations

print("Dictionary Operations in Python")

# 1. Creating a Dictionary
student = {
    "Name": "Alice",
    "Age": 25,
    "City": "New York"
}
print("\nOriginal Dictionary:", student)

# 2. Accessing Values
print("Name is:", student["Name"])
print("Age is:", student.get("Age"))

# 3. Updating Dictionary
student["Age"] = 26
student["Profession"] = "Engineer"
print("\nAfter Updating:", student)

# 4. Removing Items
city_removed = student.pop("City")
print("Removed City:", city_removed)

del student["Name"]
print("After Deleting Name:", student)

student.clear()
print("After Clearing Dictionary:", student)

# 5. Merging Two Dictionaries
d1 = {"x": 10, "y": 20}
d2 = {"z": 30}

combined = {**d1, **d2}
print("\nMerged Dictionary:", combined)
