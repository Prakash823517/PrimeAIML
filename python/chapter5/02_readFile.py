f = open("chapter5/sample.txt", "r") # file object

data1 = f.readline() # it reads one line of code
print(data1)
print(type(data1))
data2 = f.readline() 
print(data2)






# after opening we always need to close the file 
f.close()