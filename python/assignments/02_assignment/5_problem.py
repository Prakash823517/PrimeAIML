def sumOfDigit(num):
    sum = 0
    while(num > 0):
        lastDigit = num % 10;
        sum += lastDigit
        num = num // 10
    return sum



num = int(input("enter the number: "));
print(sumOfDigit(num))