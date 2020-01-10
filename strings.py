# single line string with double quote
course = "Learning single line string with double quote"
print(course)

# single line string with single quote
course = 'Learning single line string with single quote'
print(course)

# multiple line string with double quote
course = """
Hi,
This is Larry.
Learning multiple line string with double quote

Thanks
"""
print(course)

# multiple line string with single quote
course = '''
Hi,
This is Larry.
Learning multiple line string with single quote

Thanks
'''
print(course)

# get char using index
course = "Python for Beginners"
print(course[0])  # 0 is starting point
print(course[-1])  # -1 is ending point

# we can tell start point and length of char using colon (:)
print(course[0:3])
print(course[:5])  # default starting point 0
print(course[2:])  # print rest of all chars
print(course[1:-1])  # print index 1 to exclude last 1

