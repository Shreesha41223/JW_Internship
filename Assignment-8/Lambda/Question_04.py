# 4) Write a Python program to find if a given string starts with a given character using Lambda.

list_of_strings = ['Python', 'Java', 'C++', 'C#', 'Ruby', 'Perl', 'PHP', 'JavaScript']
character = 'P'
print("Original list of strings:", list_of_strings)

result = list(filter(lambda x: x[0] == character, list_of_strings))
print("Strings starting with character 'P':", result)