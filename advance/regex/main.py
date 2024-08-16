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