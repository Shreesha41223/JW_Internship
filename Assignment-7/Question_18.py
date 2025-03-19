# 18. Write a Python program to check if all dictionaries in a list are empty or not.
# Sample list : [{},{},{}]
# Return value : True
# Sample list : [{1,2},{},{}]
# Return value : False

list1 = [{},{},{}]
list2 = [{1,2},{},{}]
print("Original list 1 : ", list1)
print("Original list 2 : ", list2)
empty = True
for dictionary in list1:
    if dictionary:
        empty = False
        break
if empty:
    print("All dictionaries in the list 1 are empty.")
else:
    print("All dictionaries in the list 1 are not empty.")

empty = True
for dictionary in list2:
    if dictionary:
        empty = False
        break
if empty:
    print("All dictionaries in the list 2 are empty.")
else:
    print("All dictionaries in the list 2 are not empty.")