tup = (1, 2, 3, 4, 8, 10, 2, 6, 9, 3, 4, 1, 6)
list_odd = []
list_even = []

for i in tup:
    if(i % 2 == 0):
        list_even.append(i)
    else:
        list_odd.append(i)

tup_odd = tuple(list_odd)
tup_even = tuple(list_even)

print(tup_odd)
print(tup_even)
