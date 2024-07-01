"""
syntax : 

if condition1:
    block of code will execute id condtion-1 is true
elif condition2:
    block of code will execute id condtion-2 is true
elif condition3:
    block of code will execute id condtion-3 is true
    .
    .
    .
else:
    default block

"""


score = -224

if score <= 100 and score >= 0:
    if score >= 80:
        print("Class A")
    elif score >= 60:
        print("Class B")
    elif score >= 40:
        print("Class C")
    else:
        print("Sorry, You are failed.")
else:
    print("Invalid Score. Please enter a valid score between (0-100)")