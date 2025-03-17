# 15. Write a Python program to count repeated characters in a string.
# Sample string: 'thequickbrownfoxjumpsoverthelazydog'
# Expected output :
# o 4
# e 3
# u 2
# h 2
# r 2
# t 2

str1 = input("Enter a string: ")
freq = {}
for i in str1:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

freq = {k: v for k, v in sorted(freq.items() , key=lambda item: item[1], reverse=True) if v > 1} 
print("Repeated characters in the string are:")
for k, v in freq.items():
    print(k, v)