# 7) Write a Python program to sort a given matrix in ascending order according to the sum of its rows using lambda. 
# Original Matrix: [[1, 2, 3], [2, 4, 5], [1, 1, 1]] 
# Sort the said matrix in ascending order according to the sum of its rows [[1, 1, 1], [1, 2, 3], [2, 4, 5]]
#  Original Matrix: [[1, 2, 3], [-2, 4, -5], [1, -1, 1]] 
# Sort the said matrix in ascending order according to the sum of its rows [[-2, 4, -5], [1, -1, 1], [1, 2, 3]] 

matrix = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
print("Original Matrix:", matrix)

matrix.sort(key = lambda x: sum(x))
print("Sort the said matrix in ascending order according to the sum of its rows", matrix)