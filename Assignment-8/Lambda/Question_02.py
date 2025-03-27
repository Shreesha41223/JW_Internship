# 2) Write a Python program to sort a list of tuples using Lambda. 
# Original list of tuples: [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
# Sorting the List of Tuples: [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]

list_of_tuples = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
print("Original list of tuples:", list_of_tuples)

list_of_tuples.sort(key = lambda x: x[1])
print("Sorting the List of Tuples:", list_of_tuples)