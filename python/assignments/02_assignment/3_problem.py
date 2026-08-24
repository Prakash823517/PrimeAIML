def digits(num):
    if(num == 0):
        print(0)
    while(num > 0):
        print(num % 10)
        num //= 10

num = int(input("enter a  number: "))
digits(num);