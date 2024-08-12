class ATM:
    def __init__(self, pin):
        # self.p = pin # public
        self.__p = pin # private

    # def display(self):
    #     print(self.__p)

obj = ATM(1234)
# print(obj.p) # prints: 1234
# print(obj.__p) # prints: 1234
# obj.display()
print(obj._ATM__p) # namemangling system
