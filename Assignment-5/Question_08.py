# 8. Write a Python function that takes a list of words and returns the length of the longest one. 

def longest_word(words):
    return max(words, key=len)

words = input("Enter a list of words separated by space: ").split()
long_word = longest_word(words)
print("Longest word is: '" + long_word + "' with length", len(long_word))