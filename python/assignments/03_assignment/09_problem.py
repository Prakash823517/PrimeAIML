list = [1, 2, 3, 1, 2, "prakash", True, 1, 4, 2, True, "prakash", 3]

list_set = set(list)

for i in list_set:
    if(list.count(i) > 1):
        print(i)


# method 2
numbers = [1, 2, 3, 2, 4, 5, 1, 6, 3]

seen = set()
duplicates = set()

for num in numbers:

    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)

print("Repeated elements:", duplicates)


# end of program

print(list.count(1), list.count(True))  # True == 1

# True does not print bcz set consider True and 1 as same element
# True == 1 and the set will be created 
# {1, 2, 3, 4, "prakash"}