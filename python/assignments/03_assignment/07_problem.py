# str = input("enter a string: ")

# list = []

# for i in str:
#     if(i == ' '):
#         continue;
#     else:
#         list.append(i)

# num_spaces = len(str) - len(list)
# print(f"number of spaces: {num_spaces} ")

# method 2
text = input("Enter a string: ")

count = 0

for char in text:
    if char == " ":
        count += 1

print("Number of spaces:", count)