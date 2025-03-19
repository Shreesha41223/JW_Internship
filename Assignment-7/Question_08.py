# 8.  Write a Python program to sum all the items in a dictionary.

dict1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}
sum = 0
for key, value in dict1.items():
    sum += value
print("Sum of all the items in the dictionary : ", sum)