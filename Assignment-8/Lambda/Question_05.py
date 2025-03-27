# 5) Write a Python program to check whether a given string is number or not using Lambda.

list_of_strings = ['Python', 'Java', 'C++', 'C#', 'Ruby', 'Perl', 'PHP', 'JavaScript', '123', '456', '789', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
print("Original list of strings:", list_of_strings)

result = list(filter(lambda x: x.isnumeric(), list_of_strings))
print("Numbers in the list:", result)