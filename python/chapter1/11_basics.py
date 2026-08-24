myListOne = [1, 2, 3]
myListTwo = myListOne #hold same memoey reference
myListOne = 'Chai'

print(myListTwo)
print(myListOne)

myListOne = [1, 2, 3]
myListOne[0] = 33
print(myListOne)
print(myListTwo)

l1 = [0, 1, 2, 3]
l2 = l1
print(l1)
print(l2)
l1[0] = 44
print(l1)
print(l2)

p1 = [1, 2, 3]
p2 = p1
print(p1, p2)
p2 = [1, 2, 3] # here p1 and p2 holds different memory reference
p1[0] = 55
print(p1, p2)

h1 = [1, 2, 3]
h2 = h1[:] # here h1 and h2 holds different memory reference

m = [10, 8, 5] 
n = m
print(m == n) # == checks values
print(m is n)
n = [10, 8, 5] 
print(m is n) # is checks memory reference

x = 2
y = x
y = 2
print(x is y)