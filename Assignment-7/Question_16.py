# 16. Write a Python program to find the highest 3 values in a dictionary.

dict1 = {1: 2, 3: 4, 4: 3, 2: 1, 0: 6}
print("Original dictionary : ", dict1)
values = list(dict1.values())
values.sort(reverse = True)
print("Highest 3 values in the dictionary : ", values[:3])