# 16. Take inputs from user to make a list. Again take one input from user and search it in the list and delete that element, if found. Iterate over list using for loop.

lst = []
size = int(input("Enter the size of the list: "))
for i in range(size):
    lst.append(input("Enter a value: "))

print("List before: ", lst)
search = input("Enter a value to search and delete: ")
for i in lst:
    if i == search:
        lst.remove(i)
        break

print("List after:", lst)