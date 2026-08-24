squares = []

# for i in range(6):
#     squares.append(i*i)

# print(squares)


# syntax 
# output iterable condition
# sq = [i*i for i in range(6) ]

sq = [i*i for i in range(6) if i%2 != 0]
print(sq)