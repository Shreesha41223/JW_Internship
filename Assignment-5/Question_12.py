# 12. Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters.

def convert_to_uppercase(str1):
    count = 0
    for i in str1[:4]:
        if i.isupper():
            count += 1
    if count >= 2:
        return str1.upper()
    else:
        return str1
    
str1 = input("Enter a string: ")
print("Result: ",convert_to_uppercase(str1))