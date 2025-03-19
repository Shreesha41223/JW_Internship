# 19. Write a Python program to remove duplicates from a list of lists.
# Sample list : [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
# New List : [[10, 20], [30, 56, 25], [33], [40]]

list1 = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
print("Original list : ", list1)
new_list = []
for sublist in list1:
    if sublist not in new_list:
        new_list.append(sublist)

print("List after removing duplicates : ", new_list)