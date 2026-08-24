class BankAccount:
    def __init__(self, name, balance):
        self.name = name #public
        # self._balance = balance  
        # protected after applying (_) it will become protected

        self.__balance = balance # private -> data mangling

acc1 = BankAccount("Rahul Kumar", "100_000")
# print(acc1.name, acc1.balance)
#by convention we have not allowed to access protected attribute 
# but we can access them
# print(acc1.name, acc1._balance)

# private attribute cannot be accessed outside the class 
print(acc1.name, acc1.__balance) 
