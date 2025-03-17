# 20. Write a Python program to remove all consecutive duplicates of a given string.

def remove_consecutive_duplicates(str1):
    result = ""
    for i in range(len(str1)-1):
        if str1[i] != str1[i+1]:
            result += str1[i]
    return result + str1[-1]

str1 = input("Enter a string: ")
print("Result: ",remove_consecutive_duplicates(str1))