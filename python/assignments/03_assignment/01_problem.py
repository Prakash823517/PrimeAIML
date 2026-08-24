# str = input("enter the string: ")

# palindrome = True
# for i in range(int(len(str) / 2)):
#     if(str[i] != str[len(str)-i-1]):
#         palindrome = False
#         break;

# if(palindrome == True):
#     print(f"{str} is a palindrome")
# else:
#     print(f"{str} is not a palindrome")


# method 2

text = input("Enter a string: ")

reverse = ""

for char in text:
    reverse = char + reverse

if text == reverse:
    print("Palindrome")
else:
    print("Not a palindrome")

    
