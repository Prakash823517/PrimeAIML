# try, except, else, finally 
# try -> inside try block we write the code which can cause error

try:
    x = int(input("enter x: "))
    ans = 10/x
except ZeroDivisionError:
    print(f"Divide by 0 is not allowed")
except ValueError:
    print("Invalid input")
else:
    print(f"ans = {ans}")
finally:
    # finally always executes irrespective of error. it executes 
    #  either when code executes or throw exception
    print("end of program")

