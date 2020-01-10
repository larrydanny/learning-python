# ptint(x, y) like
# (0, 0), (0, 1), (0, 2)
# (1, 0), (1, 1), (1, 2)

for x in range(4):
    for y in range(3):
        print(f"({x}, {y})")

# have list of numbers [5, 2, 5, 2, 2]
# have to print "F" shape
# xxxxx
# xx
# xxxxx
# xx
# xx
numbers = [5, 2, 5, 2, 2]
print("print 'F' shape using single loop")
for number in numbers:
    print("x" * number)

print("print 'F' shape using nested loop")
for number in numbers:
    output = ''
    for count in range(number):
        output += "x"
    print(output)
