def digitCount(n):
    
    count = 0
    if(n == 0):
        count = 1
    
    while(n > 0):
        n = n//10
        count += 1
    return count
    

n = int(input("enter the number: "))
print(digitCount(n))