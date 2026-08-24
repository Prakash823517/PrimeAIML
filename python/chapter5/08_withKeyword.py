# when we use with keyword then files automatically
# close and don't need to write file.close() 

with open("chapter5/test.txt", "r") as f:
    # print(f.read())
    data = f.read()
    print(data)
    print(len(data))