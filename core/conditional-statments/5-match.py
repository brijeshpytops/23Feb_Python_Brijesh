"""
match parameter:
    case pattern1:
        # code for pattern 1
    case pattern2:
        # code for pattern 2
    .
    .
    case patterN:
        # code for pattern N
    case _:
        # default code block
"""

num = int(input("Enter a number between 1 and 3: "))
    
# match case
match num:
    # pattern 1
    case 1:
        print("One")
    # pattern 2
    case 2:
        print("Two")
    # pattern 3
    case 3:
        print("Three")
    # default pattern
    case _:
        print("Number not between 1 and 3")