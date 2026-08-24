list1 = []
list2 = []

for i in range(4):
    list1.append(int(input("enter a integer for list1: ")))
    list2.append(int(input("enter a integer for list2: ")))

print(list1, list2)

# for i in list2:
#     list1.append(i)

# sorted_list = sorted(list1)

# print(sorted_list)


result = list1 + list2
result.sort()

print("List1: ", list1)
print("List2: ", list2)
print("Merged and sorted list:", result)