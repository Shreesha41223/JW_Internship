# 8) Write a Python program to check whether a given string contains a capital letter, a lower case letter, a number and a minimum length using lambda. Minimum length : 10 input string: PaceWisd0m o/p: valid string 

input_string = "PaceWisd0m"
print("Input string:", input_string)

check = lambda x: any(x.isupper() for x in input_string) and any(x.islower() for x in input_string) and any(x.isdigit() for x in input_string) and len(input_string) >= 10
print("Valid string" if check(input_string) else "Invalid string")