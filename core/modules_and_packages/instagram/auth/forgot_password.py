def user_forgot_password():
    """This function will ask the user for their email address and then send them a password reset link"""

    email = input("Enter an email : ")
    if email == "admin@example.com":
        print("You are the admin, you can't reset your password")
    else:
        print("We have sent you a password reset link to your email")