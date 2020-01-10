names = ["Larry", "Danny", "Python", "List", "Name"]
print("Full lists:")
print(names)

print("Get name using index of lists:")
print(names[2])

print("Update 3 index text lists:")
names[3] = "React"
print(names)

print("Using range operator [start:end]:")
print("Display 2 and 3 index value means less one from end index")
print(names[2:4])

print("if no start and end index display full lists")
print(names[:])

print("if no start index, default start 0")
print(names[:3])

print("if no end index, display start to rest of all from lists")
print(names[2:])

# Write a program to find largest number in a list
numbers = [12, 2, 234, 34, 113]
largestNumber = numbers[0]
for number in numbers:
    if largestNumber < number:
        largestNumber = number
print(largestNumber)
