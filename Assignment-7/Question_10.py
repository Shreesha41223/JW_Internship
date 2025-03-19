# 10. Write a Python program to remove a key from a dictionary. 

dict1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}
print("Original dictionary : ", dict1)
key = int(input("Enter the key to remove : "))
if key in dict1.keys():
    dict1.pop(key)
    print("Dictionary after removing the key : ", dict1)
else:
    print("Key does not exist in the dictionary.")