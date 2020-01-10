number = 20
add = number + 3
add += 2  # we can add and keep the value in same variable like this
print(add)

subtract = number - 3
subtract -= 2
print(subtract)

multiply = number * 3
multiply *= 2
print(multiply)

divide = number / 2
divide /= 2
print(divide)
print(type(divide))  # this is a float
divide = number // 2  # if we want integer after divide, then use (//) instead of (/)
print(divide)
print(type(divide))  # this is a int

modulus = number % 3  # value = 2
modulus %= 2  # value = 0
print(modulus)

power = number ** 3
power **= 2
print(power)

# operation precedence
# ( parenthesis, exponentiation, multiplication, division, addition, subtraction )
x = 10 + 3 * 2 ** 2
print(x)
x = (10 + 3) * 2 ** 2
print(x)
x = (2 + 3) * 10 - 3
print(x)


