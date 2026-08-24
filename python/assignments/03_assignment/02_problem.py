# list = [1, 3, 2, 43, 8, 9]

# sum = 0
# for i in list:
#     sum += i

# avg = sum / len(list)
# print("average is: ", avg)


# mthood 2
numbers = []

n = int(input("How many numbers? "))

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

total = 0

for num in numbers:
    total += num

average = total / len(numbers)

print("Average:", average)