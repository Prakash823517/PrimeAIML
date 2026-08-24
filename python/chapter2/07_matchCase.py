color = input("enter color: ")

match color:
    case "Green":
        print("Go")
    case "Yellow":
        print("Look")
    case "Red":
        print("Stop");
    case _:
        print("Wrong color")

#for defult case use _(underscore)