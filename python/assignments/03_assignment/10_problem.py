str = input("enter a string: ")

# char_set = set()
# for i in str:
#     char_set.add(i)

char_set = set(str)

print(char_set)

print(f"length of unique character: {len(char_set)}")