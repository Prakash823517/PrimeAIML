tupl = (1, 2, 3, 4, 5)

sum = 0
for val in tupl:
    sum += val

print(sum)

tup = (1, 2, 2, 3, 2, 4)
# these methods also works for list 
print(tup.index(2))
print(tup.count(2))