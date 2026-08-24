class BankAccount:
    def __init__(self, acc_number, owner_name, balance):
        self.acc_number = acc_number
        self.owner_name = owner_name
        self.balance = balance

    def depostite(self, depo_money):
        self.balance += depo_money
        return self.balance

    def withdraw(self, withd_money):
        self.balance += withd_money
        return self.balance

    def check_balance(self):
        print(f"your current balance is {self.balance}")

acc1 = BankAccount("123", "Rahul", 10_000)
acc2 = BankAccount("234", "Amit", 8_000)
print(acc1.acc_number, acc1.owner_name, acc1.balance)