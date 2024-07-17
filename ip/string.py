# --------------------------------------------------------------------------------------


# 1] get string from the user

# 2] provide options to the user like

# sample_string = "HeLLo WorLD"

# lower PRESS - 1 = "hello world"
# upper PRESS - 2 = "HELLO WORLD"
# title PRESS - 3 = "Hello World"
# capitalize PRESS - 4 = "Hello world"
# swapcase PRESS - 5 = "hEllO wORld"

# without using string built-in methods
# also use match case


# -----------------------------------------------------------------------------------

# 1] get string from the user

# "Hello"

# uppercase == "11", "00"
# loweecase == "1", "0"


# "110110"

# new_str = ""
# for ch in input("Enter a string"):
#     vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
#     if ch.isupper() and ch not in vowels:
#         new_str += "11"
#     elif ch.islower() and ch not in vowels:
#         new_str += "1"
#     elif ch.islower() and ch in vowels:
#         new_str += "0"
#     elif ch.isupper() and ch in vowels:
#         new_str += "00"
# print(new_str)

# --------------------------------------------------------------------------------------

# name = input("Enter a something...")
# unique_ch = ""
# emp_dict = dict()
# for ch in name:
#     if ch not in unique_ch:
#         unique_ch += ch
#         emp_dict.update({ch:name.count(ch)})
# print(emp_dict)

# print(unique_ch)

