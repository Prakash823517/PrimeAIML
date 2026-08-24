nums = [1, 2, 4, 10, 3]
# for val in nums:
#     print(val)

index = 0
for val in nums:
    if(val == 10):
        print(f"index of 10 is {index}")
        break;
    index += 1