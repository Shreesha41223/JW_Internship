# 16. Write a Python program to print the index of the character in a string.

def index_of_char(str1, char):
    return str1.index(char)

str1 = input("Enter a string: ")
char = input("Enter the character: ")
print("Result: ",index_of_char(str1, char))