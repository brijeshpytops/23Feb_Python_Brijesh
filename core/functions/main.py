"""
In Python, a function is a block of reusable code that performs a specific task. Functions allow you to organize your code into manageable sections, making it more readable and maintainable. 

Defining a Function

To define a function in Python, you use the def keyword, followed by the function name, parentheses (), and a colon :. Inside the parentheses, you can include parameters that the function can accept. The code block that follows (indented) contains the function's operations.

Syntax:

def function_name(parameters):
    code block

def function_name(parameters):
    # Function body
    # Code to be executed
    return result

function_name(values)
"""

# a = 10
# b = 20


# print(a + b)

# c = 30
# d = 40
# e = 50

# print(c + d + e)

# def sum_(a,b,c):
#     print(a+b+c)

# sum_(10,20,30)

# def bill(potato, tomato=50):
#     print(tomato + potato)

# bill(120, 120)

# Postional para
# def sum(a,b):
#     print(a+b)

# sum(10, 20)

# default/keyword para
# def bill(potato, tomato=50):
#     print(tomato + potato)

# bill(120, 120)

# variable length para
# *args
# **kwargs

# def sum(*nums):
#     print(type(nums))

# sum('sih', 'chito', 'vandro', 'biladi', 'magar')

# def sum_(*nums):
#     print(sum(nums))

# sum_(1,2,3,4,5,6,7,8,9,10,45, 100)

# def bill(**products):
#     total_amount = 0
#     for key, value in products.items():
#         total_amount += value
#         print(key, value)
#     print("Total Amount = ", total_amount)

# bill(tomato=1000, potato=20, book=2, gold_milk=33, amul_tTop=21)

# x = 10 # global var

# def text():
#     global x
#     x = 20 # local var
#     print(x)

# text()
# print(x)

# var = lambda x, y : x + y
# print(var(10,20))


# def length(func):
#     def inner():
#         result = len(func())
#         print(result)
#     return inner

# def swap_case(func):
#     def inner():
#         result = func().swapcase()
#         print(result)
#         return  result
#     return inner

# def upper_case(func):
#     def inner():
#         result = func().upper()
#         print(result)
#         return result
#     return inner


# @length
# @swap_case
# @upper_case
# def name():
#     return input("Enter your name: ")
# name()

nums = [1,2,3,4,5]
# print(list(map(lambda x:x*x*x, nums)))

# print(list(filter(lambda num: num%2!=0, nums)))

