import re

# txt = "The rain in Spain"
# x = re.search("^The.*Spain$", txt)
# print(x)

data = "zd,.jgfmh 23-12-1996 zd,.jgfmh 3-1-2000 zd,.jgfmh 02/3/2020"

# pattern = r"\b\d{2}-\d{2}-\d{4}\b"
# pattern = r"\b\d{1,2}-\d{1,2}-\d{4}\b"
# pattern = r"\b\d{1,2}[-/]\d{1,2}[-/]\d{4}\b"
# print(re.findall(pattern, data))

# pattern = "\b[a-zA-Z0-9_-+.]@[a-zA-Z0-9-].[a-zA-Z]\b"
# pattern = "^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,6}$"


# txt = "The rain in Spain"
# x = re.search("\s", txt)

# print("The first white-space character is located in position:", x.start()) 

# txt = "The rain in Spain"
# x = re.split("\s", txt)
# print(x)

# txt = "The rain in Spain"
# x = re.split("i", txt)
# print(x)


# def validate_mobile(number):
#     # Regex pattern for a simple validation (e.g., for Indian numbers)
#     pattern = r'^[6-9]\d{9}$'
    
#     if re.match(pattern, number):
#         return True
#     else:
#         return False

# # Test the function
# numbers_to_test = ["9876543210", "1234567890", "+91 9876543210"]

# for number in numbers_to_test:
#     if validate_mobile(number):
#         print(f"{number} is a valid mobile number.")
#     else:
#         print(f"{number} is not a valid mobile number.")



# text = """
#     Contact me at +1 234-567-8901 or at my office number +91 9876543210.
#     You can also reach my assistant at 7896541230.
# """

# # Regex pattern to match mobile numbers
# pattern = r'\+?\d{1,3}[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}'

# # Substitute the mobile numbers with [MOBILE]
# result = re.sub(pattern, '[MOBILE]', text)

# print("Modified Text:")
# print(result)

