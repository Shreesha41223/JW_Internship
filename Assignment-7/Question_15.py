# 15. Write a Python program to combine two dictionary adding values for common keys.
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})

dict1 = {'a': 100, 'b': 200, 'c':300}
dict2 = {'a': 300, 'b': 200, 'd':400}
print("First dictionary : ", dict1)
print("Second dictionary : ", dict2)
dict3 = {}

for key in dict1.keys():
    if key in dict2.keys():
        dict3[key] = dict1[key] + dict2[key]
    else:
        dict3[key] = dict1[key]

for key in dict2.keys():
    if key not in dict1.keys():
        dict3[key] = dict2[key]
        
print("Combined dictionary : ", dict3)