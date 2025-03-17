# 2. Write a Python program to count the number of characters (character frequency) in a string. 
# Sample String : google.com'
# Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}

str = input("Enter a string: ")
freq = {}
for i in str:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

freq = {k: v for k, v in sorted(freq.items(), key=lambda item: item[1], reverse=True)}
print("Character frequency in the string is:", freq)