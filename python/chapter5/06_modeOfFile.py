f = open("chapter5/sample.txt", "r+")
f.write("123") # the pointer will be in start so
# it will erase the starting 3 character and overwrite by 123 
print(f.read())

f.close()