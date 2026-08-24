# to access private attribute outside the calss getter and setter 
# methods are used

class BankAccount:
    def __init__(self, name, balance):
        self.name = name #public
        self.__balance = balance

    def get_balance(self): #getter
        return self.__balance

    def set_balance(self, newBalance): #setter
        self.__balance = newBalance

    

acc1 = BankAccount("Rahul Kumar", 100_000)

print(acc1.name, acc1.get_balance())
acc1.set_balance(200_000)
print(acc1.name, acc1.get_balance())

#  direct method 
# to access private Attribute 
print(acc1.name, acc1._BankAccount__balance)

