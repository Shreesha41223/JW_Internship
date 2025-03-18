# 7. Write a Python program that counts the number of elements within a list that are greater than 30.

size = int(input("Enter the size of the list: "))
lst = []   
for i in range(size):
    lst.append(int(input("Enter a number: ")))

count = 0
for i in lst:
    if i > 30:
        count += 1

print(f"Number of elements greater than 30: {count}")