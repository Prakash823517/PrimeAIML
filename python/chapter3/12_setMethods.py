s = {1, 2, 2, 2, 3}

s.add(5)
s.remove(1)
print(s)
# s.clear()

s.pop() # removes a random element
print(s)

s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 8, 9, 10}

print(s1.intersection(s2))
print(s1.union(s2))