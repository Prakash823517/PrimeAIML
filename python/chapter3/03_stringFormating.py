a = 5
b = 10
sum = a + b

#normal formatting
print("language is {}".format("Python"))
print("sum of {} & {} is {}" .format(a, b, sum))

#index based formating
print("sum of {1} & {0} is {2}" .format(a, b, sum))

#values based formating
print("values of vars {a} & {b}".format(a=5, b=10))


# f-strings
print(f"sum of {a} & {b} is {a + b}")
