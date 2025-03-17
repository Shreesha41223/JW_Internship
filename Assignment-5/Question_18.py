# 18. Write a Python program to swap comma and dot in a string.
# Sample string: "32.054,23"
# Expected Output: "32,054.23"

str1 = input("Enter a string: ")
str1 = str1.replace(",", "comma")
str1 = str1.replace(".", "dot")
str1 = str1.replace("comma", ".")
str1 = str1.replace("dot", ",")
print("Result: ",str1)