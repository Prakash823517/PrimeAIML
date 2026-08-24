# tuples -> immutable sequence of values 
# ordered

tup = (1, 2, 3.14, 4, 5, "abc")

print(tup)
print(len(tup))
print(type(tup))
print(tup[2])

# tuple slicing is same as string slicing 
print(tup[0:3])

# tup[1] = 10 we can not change(assign) tuple
# bcz tuples are immutable

# we can't assign tuple by a single value 
# bcz it assumes, it as a mathematical expression 

tup2 = (1)
tup3 = ("abc")
print(type(tup2))
print(type(tup3))

# to assign single value in tuple we use comma
tup4 = (1,)
tup5 = ("abc",)
print(type(tup4))



