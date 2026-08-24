# sets -> collection of unique elements
# where all elements are immutable 
# sets are mutable and unordered

s = {1, 2, 2, 2, 3, 7, 4}
print(s)
print(type(s))
print(len(s))

s.add(0)
print(s)

# for empty set 
empty_set = set()
print(type(empty_set))

# se = {} # this is empty dictionary not set 
