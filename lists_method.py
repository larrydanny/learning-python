numbers = [3, 2, 7, 4, 5, 1]

print("Add new value 22 at the end on the list")
numbers.append(22)
print(numbers)

print("Add new value 10 at 2 index on the list")
numbers.insert(2, 22)  # 2 is index and 10 is value
print(numbers)

print("Get index of given item 7")
print(numbers.index(7))

print("If given item not in lists index method given error")
print("So, if we print print(numbers.index(70))")
print("Getting below error")
# print(numbers.index(70))
print("""
Traceback (most recent call last):
  File "lists_method.py", line 17, in <module>
    print(numbers.index(70))
ValueError: 70 is not in list
""")

print("Check item exist or not in list")
print(70 in numbers)

print("Count how many time add the given item 22 in list")
print(numbers.count(22))

print("Sort the list")
numbers.sort()
print(numbers)

print("Reverse the list")
numbers.reverse()
print(numbers)

print("Copy the list into new variable")
numbers2 = numbers.copy()
numbers.append(11)
print("Main => ", numbers)
print("Copy => ", numbers2)

print("Remove given item 7 of the list")
numbers.remove(7)
print(numbers)

print("Remove last item of the list")
numbers.pop()
print(numbers)

print("Remove all items of the list")
numbers.clear()
print(numbers)

# Write a program to remove the duplicates in a list
print("Write a program to remove the duplicates in a list")
# numbers = [4, 3, 6, 2, 5, 3, 7, 8, 2]
numbers = [2, 2, 4, 6, 3, 4, 6, 1]
print(numbers)
for number in numbers:
    count = numbers.count(number)
    if count > 1:
        numbers.remove(number)
print(numbers)  # this one given right output but indexing is different

# Right one
numbers = [2, 2, 4, 6, 3, 4, 6, 1]
uniques = []
print(numbers)
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)


