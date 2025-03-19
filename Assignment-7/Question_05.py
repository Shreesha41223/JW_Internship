# 5. Write a Python program to iterate over dictionaries using for loops.

dict1 = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print("Original dictionary : ", dict1)
print("Iterating over dictionary using for loop : ")
for key, value in dict1.items():
    print(key, ":", value )