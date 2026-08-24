with open("assignments/05_assignment/log.txt", 'a') as f:
    f.write("Program run successfully\n")

with open("assignments/05_assignment/log.txt", "r") as f:
    print(f.read())