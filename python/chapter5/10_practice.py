data = True
line = 1
word = "python"
with open("chapter5/test2.txt", "r") as f:
    while data:
        data = f.readline()
        if("python" in data):
            print(f"{word} found at line {line}")
            break

        line += 1
    
    
    
