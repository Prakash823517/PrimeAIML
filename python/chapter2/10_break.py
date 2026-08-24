# break -> break is used to terminate the loop

# continue -> continue skip the current iteration
# and move on to next iteration 

i = 1
while (i <= 5):
    if(i % 3 == 0):
        break;
    print(i)
    i += 1

print("outside loop now")