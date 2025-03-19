# 7. Write a Python script to merge two Python dictionaries.

dict1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}
dict2 = {1: 60, 7: 70, 8: 80, 9: 90, 10: 100}
dict3 = {}
dict3.update(dict1)
dict3.update(dict2)
print("Dictionary 1 : ", dict1)
print("Dictionary 2 : ", dict2)
print("Merged dictionary : ", dict3)