"""
Logical Operators
Logical operators are used to combine conditional statements.

• and : Logical AND (e.g., a and b)
• or : Logical OR (e.g., a or b)
• not  : Logical NOT (e.g., not a)

A B C and or
T T T T   T
F T T F   T
T F T F   T
T T F F   T
F F F F   F

A not
T F
F T

"""

c1 = True
c2 = False
c3 = 1 # True
c4 = 0 # False
c5 = 10 < 29 # True
c6 = not c3 # False

# print(c1 and c2) # False
# print(c1 and c3) # True
# print(c1 and c4) # False
# print(c1 and c5) # True
# print(c1 and c6) # False
# print((c1 and c5) or (not c4) and (c6 and c2) and not c3)
print(True or True and False and not c3)
print(True)