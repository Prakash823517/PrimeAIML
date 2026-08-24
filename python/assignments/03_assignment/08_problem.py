list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8 , 1, 2]

set1 = set(list1)
set2 = set(list2)

common_elem = set1.intersection(set2)

if(len(common_elem) == 0):
    print("no common element")
else:
    print("common element")
print(common_elem)