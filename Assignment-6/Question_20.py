# 20.You are given with a list of integer elements. Make a new list which will store square of elements of previous list.

lst = [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
squared = []

for i in lst:
    squared.append(i ** 2)

print(f"List: {lst}")
print(f"Squared: {squared}")