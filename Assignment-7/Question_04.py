# 4. Write a Python script to check if a given key already exists in a dictionary.

dict1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}
print("Original dictionary : ", dict1)
key = int(input("Enter the key to check : "))
if key in dict1.keys():
    print("Key exists in the dictionary.")
else:
    print("Key does not exist in the dictionary.")