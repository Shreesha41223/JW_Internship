# 13. Write a Python program to remove duplicates from Dictionary.

dict1 = {1: 2, 3: 4, 4: 3, 2: 1, 0: 6, 5: 4, 6: 2, 7: 1}
print("Original dictionary : ", dict1)
dict2 = {}
for key, value in dict1.items():
    if value not in dict2.values():
        dict2[key] = value