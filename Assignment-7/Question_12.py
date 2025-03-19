# 12. Write a Python program to get the maximum and minimum value in a dictionary.

dict1 = {1: 2, 3: 4, 4: 3, 2: 1, 0: 6}
print("Original dictionary : ", dict1)
max_value = max(dict1.values())
min_value = min(dict1.values())
print("Maximum value in the dictionary : ", max_value)
print("Minimum value in the dictionary : ", min_value)