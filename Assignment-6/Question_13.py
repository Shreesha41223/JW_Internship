# 13. Take 10 integers from keyboard using loop and print their average value on the screen.

total = 0
for i in range(10):
    num = int(input("Enter a number: "))
    total += num

print(f"Average: {total / 10}")