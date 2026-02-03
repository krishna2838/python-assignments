print("2.1 Create and Access Set Elements")
first_set = {10, 20, 30, 40, 50}
print("Set 1:", first_set)

print("Elements inside Set 1:")
for value in first_set:
    print(value, end=" ")
print()

print("\n2.2 Union of the Elements")
second_set = {40, 50, 60, 70, 80}
print("Set 2:", second_set)

combined_set = first_set | second_set
print("Union Result:", combined_set)

print("\n2.3 Intersection of the Elements")
common_values = first_set & second_set
print("Intersection Result:", common_values)

print("\n2.4 Difference of the Elements")
only_first = first_set - second_set
print("Set 1 - Set 2:", only_first)

only_second = second_set - first_set
print("Set 2 - Set 1:", only_second)
