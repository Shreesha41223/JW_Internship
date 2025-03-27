# 10) Write a Python program to sort a given mixed list of integers and strings using lambda. Numbers must be sorted before strings. 
# Original list: [19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1] 
# Sort the said mixed list of integers and strings: [1, 10, 12, 19, 'blue', 'green', 'green', 'red', 'white']

list_of_mixed = [19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]
print("Original list of mixed integers and strings:", list_of_mixed)

list_of_mixed.sort(key = lambda x: (isinstance(x, str), x))
print("Sort the said mixed list of integers and strings:", list_of_mixed)