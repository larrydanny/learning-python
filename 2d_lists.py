matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("I want to print 5")
print(matrix[1][1])

print("I want to change 9 => 90")
matrix[2][2] = 90
print(matrix[2][2])

print("I want to print all values")
for row in matrix:
    for item in row:
        print(item)
