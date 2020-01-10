birthYear = input("Birth Year: ")
print(type(birthYear))
age = 2020 - int(birthYear)
print(age)
print(type(age))

# Task: Ask user their weight (in pound), convert to kilogram and print
weight = input("Weight in pound? ")
print(type(weight))
kg = int(weight) * 0.45
print("Your weight in kilogram is " + str(kg))
print(type(kg))
