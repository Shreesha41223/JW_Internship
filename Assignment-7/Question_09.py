# 9. Write a Python program to multiply all the items in a dictionary.

dict1 = {1: 2, 3: 4, 4: 3, 2: 1, 0: 6}
print("Original dictionary : ", dict1)
product = 1
for key, value in dict1.items():
    product *= value
print("Product of all the items in the dictionary : ", product)
