# 11. Write a Python program to sort a dictionary by key.

dict1 = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print("Original dictionary : ", dict1)
asc_dict = dict(sorted(dict1.items()))
print("Dictionary in ascending order by key : ", asc_dict)