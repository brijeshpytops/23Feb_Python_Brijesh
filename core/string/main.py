"""
a string is a sequence of characters used to represent text. Strings are one of the most commonly used data types and are crucial for various operations such as text processing, file handling, and data manipulation.
"""

# syntax :
# str_name = 'djgfjg'
# str_name = "djgfjg"
# str_name = '''hfjsgfjsdhgj'''
# str_name = """sjghdghdfgdh"""

# name = "name is 'brijesh gondaliya'"
# name = 'name is "brijesh gondaliya"'

# name = 'name is \'brijesh gondaliya\''
# print(name)

# print("\"")
# print("\'")
# print("\\")
# print("\\\\")
# print("\tbrijesh")

name = "python"
# print(len(name))

# print(type(name))

# print(name)

# indexing (+/-)
# print(name[0])
# print(name[1])
# print(name[-1])
# print(name[-2])

# slicing (+/-)
# print(name[start:end-1:step-1])
# print(name[2:5])
# print(name[::2])
# print(name[::-1])
# print(name[-2:-5:-1])
# print(name[0:5:2])
# print(name[::-1][-2:-5:-1])

# print(dir(name))
# print(len(dir(name)))

name = "TopS TeCHnOLOgY PVt. LTd."
# print(name.lower().count('t'))

# print(name.index('e'))

# print(name.upper())
# print(name.lower())
# print(name.title())
# print(name.capitalize())
# print(name.swapcase())

# print(name.casefold())

center = "*"
# print(len(center.center(2)))
# print(center.center(10, '-'))

name = '     python is is this    '
# print(name.lstrip())
# print(name.rstrip())
# print(name.strip())
# print(name.replace(" ", ""))

# print(name.count('is'))

# password = "$#%^$&^^"

# print(not password.isalnum())
# print(password.isalpha())
# print(password.isalnum())
# print(password.isnumeric())
# print(password.isupper())

fname = 'brijesh'
lname = 'gondaliya'
# print(fname+ ' ' + lname)
# print(fname*4)

# for num in range(5):
#     print(" *"*(5-num), " *"*(num+1))

name = "Python"
pages = 300
price = 5354.54
print("Book name is Python and it has 300 pages and price is 5354.54")
# print(f"Book name is {name} and it has {pages} pages and price is {price}")
# print("Book name is {} and it has {} pages and price is {}".format(name, pages, price))
# print("Book name is {1} and it has {0} pages and price is {2}".format(name, pages, price))
# print("Book name is %s and it has %d pages and price is %.2f" % (name, pages, price))
