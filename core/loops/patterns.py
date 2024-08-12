# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5

# num = 5
# for row in range(1, num+1):
#     for col in range(1, num+1):
#         print(col, end=' ')
#     print()

# print("hello", end='-')
# print("end", end='|')
# print("end-1")

# In Python, the end keyword is not used directly within an if statement itself. However, it is commonly used as an argument in the print function to control what is printed at the end of the output.

# Understanding end in the print Function
# By default, the print function in Python ends its output with a newline character (\n). This means that each call to print outputs on a new line. The end parameter allows you to change this behavior.


# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5

# num = 5
# for row in range(1, num+1):
#     for col in range(1, row+1):
#         print(col, end=' ')
#     print()

# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

# num = 5
# for row in range(1, num+1):
#     for col in range(1, row+1):
#         print(row, end=' ')
#     print()

# A - 65(ASCII)
# Z - 90(ASCII)
# a - 97(ASCII)
# z - 122(ASCII)

# num = 5
# for row in range(1, num+1):
#     for col in range(1, row+1):
#         print(chr(row + 64), end=' ')
#     print()

# print(ord('A'))

# num = 5
# for row in range(1, num+1):
#     for col in range(1, num+1):
#         if row % 2 == 0:
#             print("0", end=' ')
#         else:
#             print("1", end=' ')
#     print()


# num = 5
# for row in range(1, num+1):
#     for col in range(1, num+1):
#         if col % 2 == 0:
#             print("0", end=' ')
#         else:
#             print("1", end=' ')
#     print()

# *
# * *
# * * *
# * * * *
# * * * * *
# num = 5
# for row in range(1, num+1):
#     for col in range(1, row+1):
#         print("*", end=' ')
#     print()

# * * * * *
# * * * *
# * * *
# * *
# *
num = 5
for row in range(1, num+1):
    for col in range(1, num-row+2):
        print("*", end=' ')
    print()



# * 
#   * 
#     * 
#       * 
#         * 
# * * * * 
# * * * 
# * * 
# * 


num = 5
for row in range(1, num+1):
    
    for col in range(1, row+1):
        if row == col:
            print("*", end=' ')
        else:
            print(" ", end=' ')
    print()
for row in range(1, num+1):
    for col in range(1, num-row+1):
        print("*", end=' ')
    print()


# * 
#   * 
#     * 
#       * 
#         * 
#       * 
#     * 
#   * 
# * 

num = 5
for row in range(1, num+1):
    
    for col in range(1, row+1):
        if row == col:
            print("*", end=' ')
        else:
            print(" ", end=' ')
    print()
for row in range(1, num+1):
    for col in range(1, num-row+1):
        if num-row == col:
            print("*", end=' ')
        else:
            print(" ", end=' ')
    print()


#             * 
#           *   * 
#         *       * 
#       *           * 
#     *               * 
#   *                   * 
# *                       * 
#   *                   * 
#     *               *   
#       *           *     
#         *       *       
#           *   *         
#             *           


# num = 7
# for row in range(1, num+1):
#     for col in range(num-row+1, 1, -1):
#         print(" ", end=' ')
#     for col in range(1, row+1):
#         if col == 1:
#             print("*", end=' ')
#         else:
#             print(" ", end=' ')
#     for col in range(2, row+1):
#         if row == col:
#             print(f"*", end=' ')
#         else:
#             print(" ", end=' ')
#     print()
# for row in range(1, num+1):
#     for col in range(1, row+1):
#         print(" ", end=' ')
#     for col in range(num-row+1, 1, -1):
#         if col == num-row+1:
#             print("*", end=' ')
#         else:
#             print(" ", end=' ')
#     for col in range(2, num):
#         if num-row == col:
#             print(f"*", end=' ')
#         else:
#             print(" ", end=' ')
#     print()


#       *
#      * *
#     * * *
#    * * * *
#   * * * * *
#    * * * *
#     * * *
#      * *
#       *

num = 5
for row in range(1, num+1):
    print(" "*(num-row), f" *"*row)
for row in range(2, num+1):
    print(" "*(row-1), " *"*(num-row+1))
   
#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 
#  * * * * 
#   * * * 
#    * * 
#     * 



num = 5

for row in range(2*num-1):
    if row < num:
        if row == 0:
            print(' ' * (num - row - 1) + '*')
        else:
            print(' ' * (num - row - 1) + '*' + ' ' * (2*row-1) + '*')
    else:
        if row == 2*num-2:
            print(" " * (row-num+1) + '*')
        else:
            print(" " * (row-num+1) + '*' + ' ' * (2*(2*num-row-2)-1) + '*')


#     *
#    * *
#   *   *
#  *     *
# *       *
#  *     *
#   *   *
#    * *
#     *


num = 5 

for row in range(2*num-1):
    if row < num:
        print(' ' * (num - row - 1) + '* ' * (row + 1))
    else:
        print(' ' * (row - num + 1) + '* ' * (2*num - row - 1))


#       *
#      * *
#     * * *
#    * * * *
#   * * * * *

# num = 5
# for row in range(1, num+1):
#    print(" "*(num-row), f" *"*row)


#      *
#     **
#    ***
#   ****
#  *****

# num = 5
# for row in range(1, num+1):
#    print(" "*(num-row), f"*"*row)


# *
# **
# ***
# ****
# *****

# num = 5
# for row in range(1, num+1):
#    print("*"*row)
