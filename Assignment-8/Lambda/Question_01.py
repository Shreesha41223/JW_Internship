# 1) Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, also create a lambda function that multiplies argument x with argument y and print the result.
#  Sample Output: 25 48 

add = lambda x: x + 15
multiply = lambda x, y: x * y

print(add(10))
print(multiply(4, 12))