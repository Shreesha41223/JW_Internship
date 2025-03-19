# 20. Write a Python program to extend a list without append.
# Sample data: [10, 20, 30]
# [40, 50, 60]
# Expected output : [40, 50, 60, 10, 20, 30]

list1 = [10, 20, 30]
list2 = [40, 50, 60]
print("Original list 1 : ", list1)
print("Original list 2 : ", list2)
list1[:0] = list2
print("List after extending without append : ", list1)