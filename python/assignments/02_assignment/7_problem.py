while(True):
    user_input = input("enter a number ot type Quit: ")
    if(user_input != "Quit"):
        if(int(user_input) > 0):
            print("positive number");
        elif(int(user_input) < 0):
            print("negative number")
        else:
            print("zero");
    else:
        break;