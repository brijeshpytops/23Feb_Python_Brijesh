"""
In Python, data types are classifications that dictate how data is stored and manipulated in a program. Each data type specifies the type of operations that can be performed on the data and how it is stored in memory.

Basic Data Types : 
    Numeric Types:
        int: Represents integers. E.g., 1, 100, -23.
        float: Represents floating-point numbers (decimal values). E.g., 3.14, -2.7.
        complex: Represents complex numbers with real and imaginary parts. E.g., 3+4j

    Boolean Type:
        bool: Represents the boolean values True and False.

    String Type:
        str: Represents sequences of characters (text). Strings are immutable.

Sequence Types :
    list: Represents an ordered collection of items, which can be of any type. Lists are mutable. E.g. list_name = [], list()

    tuple: Represents an ordered collection of items, similar to lists, but tuples are immutable. E.g. tuple_name = (), tuple()

    range: Represents a sequence of numbers, commonly used in loops. It is immutable.
    E.g. range_name = range()

Set Types:
    set: Represents an unordered collection of unique items. Sets are mutable.
    E.g. set_name = {1,2,3,4}, set()

    frozenset: Represents an immutable version of a set. E.g. frozeset_name = fronzenset()

Mapping Type:
    dict: Represents an unordered collection of key-value pairs. Dictionaries are mutable.
    E.g. dict_name = {'key1':'value1', 'key2':'value2',...}

Other Types:
    bytes: Represents immutable sequences of bytes. Typically used for binary data.
    bytearray: Represents mutable sequences of bytes.
    memoryview: Provides a view of the data of an object that supports the buffer protocol without copying it.

None Type:
    None: Represents the absence of a value or a null value. It is the only value of the NoneType.
"""

age = 24
# print(type(age))

price = 2356.4543
# print(type(price))

name = "python"
# print(type(name))

# nums = [1,2,3,4,3]
# print(type(nums))
# nums_tuple = (1,2,3,4,3)
# nums_range = range(1,10)

# numbers = {1,2,3}
# frozen_numbers = frozenset({1,2,3})

# dict_name = {
#     "name": "python",
#     "age": 24
# }

# chamn =32
# print(chamn)