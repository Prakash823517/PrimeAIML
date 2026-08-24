while(True):

    print("Guess a number between 1 to 10")
    num = int(input("guess a number: "))

    if(num == 5):
        print("Correct");
        break;
    elif(num > 5):
        print("Too high")
    else:
        print("Too low")
    
