# 9) Write a Python program to find the elements of a given list of strings that contain specific substring using lambda. 
# Original list: ['red', 'black', 'white', 'green', 'orange'] 
# Substring to search: ack Elements of the said list that contain specific substring: ['black'] Substring to search: abc Elements of the said list that contain specific substring: [] 

list_of_strings = ['red', 'black', 'white', 'green', 'orange']
print("Original list of strings:", list_of_strings)

substring = 'ack'
result = list(filter(lambda x: substring in x, list_of_strings))
print("Elements of the said list that contain specific substring", substring, ":", result) 

substring = 'abc'
result = list(filter(lambda x: substring in x, list_of_strings))
print("Elements of the said list that contain specific substring",substring,":", result)