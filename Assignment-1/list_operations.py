print("1.1 Create and Access List Elements")
numbers = [10, 20, 30, 40, 50]
print("Original List:", numbers)
print("Element at Index 2:", numbers[2])

print("\n1.2 Add and Remove List Elements")
numbers.append(60)
print("After Appending 60:", numbers)

numbers.insert(1, 15)
print("After Inserting 15 at Index 1:", numbers)

numbers.remove(40)
print("After Removing 40:", numbers)

last_value = numbers.pop()
print("Removed Last Element:", last_value)
print("List Now:", numbers)

print("\n1.3 Sort List Elements")
numbers.sort()
print("Ascending Order:", numbers)

numbers.sort(reverse=True)
print("Descending Order:", numbers)

print("\n1.4 Reverse List Elements")
numbers.reverse()
print("After Reversing:", numbers)
