# 19. Write a Python program to find smallest and largest word in a given string.

def smallest_and_largest_word(str1):
    words = str1.split()
    smallest = words[0]
    largest = words[0]
    for word in words:
        if len(word) < len(smallest):
            smallest = word
        if len(word) > len(largest):
            largest = word
    return smallest, largest

str1 = input("Enter a string: ")
smallest, largest = smallest_and_largest_word(str1)
print("Smallest word:", smallest)
print("Largest word:", largest)