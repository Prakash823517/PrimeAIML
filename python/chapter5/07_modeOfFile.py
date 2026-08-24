f = open("chapter5/text.txt", "a+")

f.write("123") 
print(f.read())
# it does not read anything bcz in append mode 
# pointer is at the end of data so 
# no data is available for reading so it doesn't print
# anything

f.close()