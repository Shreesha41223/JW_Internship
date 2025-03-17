# 4. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
# Sample String : 'restart'
# Expected Result : 'resta$t'

str1 = input("Enter a string: ")
first_char = str1[0]
str1 = str1.replace(first_char, '$')
print("Result: ",first_char + str1[1:])