# if temperature is greater than 30
# it's a hot day
# otherwise if it's less than 10
# it's a cold day
# otherwise
# it's neither hot nor cold
temperature = 30

if temperature > 30:
    print("It's a hot day")
elif temperature < 10:
    print("It's a cold day")
else:
    print("It's neither hot nor cold")

# if name less than 3 characters long
# name must be at least 3 characters
# otherwise if more than 50 characters long
# name can be maximum of 50 characters
# otherwise
# name looks good!
name = "name must be at least 3 characters otherwise if more than 50 characters long"
print(len(name))

if len(name) < 3:
    print("Name must be at least 3 characters")
elif len(name) > 50:
    print("Name can be maximum of 50 characters")
else:
    print("Name looks good!")
