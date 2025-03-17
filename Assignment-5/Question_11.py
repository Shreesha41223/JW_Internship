# 11. Write a Python function to reverses a string if it's length is a multiple of 4.

def reverse_string(str1):
    if len(str1) % 4 == 0:
        return str1[::-1]
    else:
        return str1
    
str1 = input("Enter a string: ")
print("Result: ",reverse_string(str1))