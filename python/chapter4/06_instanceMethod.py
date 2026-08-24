class Laptop:
    storage_type = "ssd"
    def __init__(self, RAM, storage):
        self.RAM = RAM
        self.storage = storage

    @classmethod
    def get_storage_type(cls): # class methods
        print(f"storage type = {cls.storage_type}")

        # it will give error bcz RAM is not in class
        # print(f"storage type = {cls.storage_type}  {cls.RAM}")

    def get_info(self): # instance method
        print(f"laptop has {self.RAM} RAM & {self.storage} {self.storage_type}")

    @staticmethod
    def calc_discount(price, discount):
        final_price = price - ((price * discount) /100)
        print(f"discounted price = {final_price}")


l1 = Laptop("16gb", "512gb")
l2 = Laptop("8gb", "256gb")

print(Laptop.get_storage_type())
l1.get_info()
l1.get_storage_type()
l1.calc_discount(40_000, 10) # 40_000 = 40000  _ is ignored