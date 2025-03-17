# 7. Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
# Sample String : 'The lyrics is not that poor!'
# 'The lyrics is poor!'
# Expected Result : 'The lyrics is good!'
# 'The lyrics is poor!'

str1 = input("Enter a string: ")
not_index = str1.find('not')
poor_index = str1.find('poor')
if not_index < poor_index:
    str1 = str1.replace(str1[not_index:poor_index+4], 'good')
print("Result: ",str1)