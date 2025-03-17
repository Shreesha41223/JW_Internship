# 17. Write a Python program to convert a string in a list.

def convert_string_to_list(str1):
    return list(str1)

str1 = input("Enter a string: ")
print("Result: ",convert_string_to_list(str1))