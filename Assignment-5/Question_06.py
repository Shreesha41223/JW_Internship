# 6. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
# Sample String : 'abc'
# Expected Result : 'abcing' 
# Sample String : 'string'
# Expected Result : 'stringly'

str1 = input("Enter a string: ")
if len(str1) < 3:
    print(str1)
elif str1[-3:] == 'ing':
    print(str1 + 'ly')
else:
    print(str1 + 'ing')