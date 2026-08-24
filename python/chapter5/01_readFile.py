f = open("chapter5/sample.txt", "r") # after opening it returns file object
data = f.read()
print(data)
print(type(data))




# after opening we always need to close the file 
f.close()