salary = int(input("enter salary: "))
if(salary < 30000):
    tax_rate = 0.05
elif(salary < 70000):
    tax_rate =  0.15
else:
    tax_rate = 0.25

tax_amount = salary * tax_rate
print(tax_amount)