# 10. Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically). 
# Sample Words : red, white, black, red, green, black
# Expected Result : black, green, red, white

str1 = input("Enter a comma separated sequence of words: ")
words = str1.split(", ")
words = list(set(words))
words.sort()
print("Result: ", ", ".join(words))