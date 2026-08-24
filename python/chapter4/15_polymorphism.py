class Teacher():
    def get_designation(self):
        print("designation = Teacher")

class Accountant():
    def get_designation(self):
        print("designation = Accountant")

# if a function has same task in different classes then we can 
# keep same name for that function in all the classes 

t1 = Teacher()
t1.get_designation()

acc1 = Accountant()
acc1.get_designation()