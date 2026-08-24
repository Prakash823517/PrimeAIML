# for a list number when value is -ve then
#  replace it by zero

nums = [-2, -4, 3, 5, 6, 2, -1, -3]

nums = [0 if val < 0 else val for val in nums]

print(nums)


words = ["hello", "python", "apnacollege"]

words = [val.upper() for val in words]
print(words)