f = open("sample.txt", "w")

# when we write in the file we overwrite the file
# it will earse the previous data present in the file
#  and write the new data
f.write("Text to overwrite \n the complete data.")

f.close()