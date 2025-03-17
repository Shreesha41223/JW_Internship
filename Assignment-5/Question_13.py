# 13. Write a Python program to check whether a string starts with any specified characters.

def check_startswith(str1, startswith):
    return str1.startswith(startswith)

str1 = input("Enter a string: ")
startswith = input("Enter the specified characters: ")
print("Result: ",check_startswith(str1, startswith))