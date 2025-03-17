# 9. Write a Python program to remove the nth index character from a nonempty string.

str1 = input("Enter a string: ")
n = int(input("Enter the index to remove character: "))
print("Result: ",str1[:n] + str1[n+1:])