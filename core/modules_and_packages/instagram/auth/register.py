def user_register():
    """This function registers a user and returns a dictionary with their information."""
    user = {}
    user['name'] = input("What is your name? ")
    user['age'] = int(input("What is your age? "))
    user['email'] = input("What is your email? ")
    return user