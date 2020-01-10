# string loop
print("String 'Python': ")
for item in "Python":
    print(item)

# string array loop
print('String Array ["Larry", "Danny", "Python"]: ')
for item in ["Larry", "Danny", "Python"]:
    print(item)

# number array loop
print('Number Array [1, 2, 3]: ')
for item in [1, 2, 3]:
    print(item)

# range function loop
print("Range function value range(5): ")
print("Range function started with 0 index")
print(" and less one the given number like 5")
for item in range(5):
    print(item)

print("Range function with start and end value range(5, 10): ")
print("Range function started with 0 index ")
print(" and less one the end number like 10")
for item in range(5, 10):
    print(item)

print("Range function with start, end and step value range(5, 10, 2): ")
print("Range function started with 0 index ")
print(" , less one the end number like 10")
print(" and print two steps forward value like 5, 7 ..")
for item in range(5, 10, 2):
    print(item)

# sum of array numbers
prices = [10, 20, 30]
total = 0
for price in prices:
    total += price
print(f"Total price: {total}")
