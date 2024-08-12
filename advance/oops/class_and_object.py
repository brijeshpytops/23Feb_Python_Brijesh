# class className:
    # attributes and properties [data member]

    # functions and methdos [member function]

# obj_name = className()

# class BIKE:
#     # attributes and properties [data member]
#     name = "R15"
    
#     # functions and methdos [member function]
#     def features(self):
#         print("break")
#         print("horn")

# b1 = BIKE()


# print(b1.name)
# b1.features()

# class BIKE:
#     def __init__(self, name):
#         self.bike_name = name

#     def display(self):
#         print(self.bike_name)

# b1 = BIKE("R15")
# b1.display()

# b2 = BIKE("HERO")
# b2.display()

class AUTH:
    class Registration:
        def __init__(self, username, email, password):
            self.ru = username
            self.re = email
            self.rp = password

        def save_data(self):
            return f"{self.ru}, Your registration is successfully done."

    class Login:
        def __init__(self, username, password):
            self.lu = username
            self.lp = password

    

auth  = AUTH()
user1 = auth.Registration("Rahul","Rahul@gmail.com", "Rahul#123")
print(user1.save_data())



