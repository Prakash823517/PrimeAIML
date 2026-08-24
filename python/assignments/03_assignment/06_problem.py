words = ["apple", "banana", "kiwi", "cherry", "mango"]

dict = {}

# for var in words:
#     dict.update({
#         var: len(var)
#     })

for word in words:
    dict[word] = len(word)

print(dict)
