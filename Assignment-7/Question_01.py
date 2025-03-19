# 1. Write a Python script to sort (ascending and descending) a dictionary by value.

dict1 = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print("Original dictionary : ", dict1)
asc_dict = {k: v for k, v in sorted(dict1.items(), key=lambda item: item[1])}
desc_dict = {k: v for k, v in sorted(dict1.items(), key=lambda item: item[1], reverse=True)}
print("Dictionary in ascending order by value : ", asc_dict)
print("Dictionary in descending order by value : ", desc_dict)
