def even_num(a, b):
    if(a >= b):
        for i in range(b, a+1):
            if(i % 2 == 0):
                print(i)

    else:
        for i in range(a, b+1):
            if(i % 2 == 0):
                print(i)

a = int(input("enter first number: "))
b = int(input("enter second number: "))

even_num(a, b)
# even(4, 8)

    