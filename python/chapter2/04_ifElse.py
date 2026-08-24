num = int(input("enter the number: "))
factor = int(input("enter factor: "))

if(num % factor == 0):
    print(f"{num} is multiple of {factor}")
else:
    print(f"{num} is not multiple of {factor}")

