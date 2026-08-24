with open("assignments/05_assignment/names.txt", "w") as f:
    for i in range(5):
        name = input(f"enter name{i+1}: ")
        f.write(name + "\n")
        

with open("assignments/05_assignment/names.txt", "r") as f:
    data = f.read()
    print(data)