try:
    with open("data.txt", "r") as f:
        data = f.read()
       
except FileNotFoundError:
    print("File not found!")

else:
    print(data)

