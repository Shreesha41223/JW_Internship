# 15. Take integer inputs from user until he/she presses q ( Ask to press q to quit after every integer input ). Print average and product of all numbers.

total = 0
product = 1
count = 0
while True:
    num = input("Enter a number or 'q' to quit: ")
    if num == 'q':
        break
    num = int(num)
    total += num
    product *= num
    count += 1

if count == 0:
    print("No numbers entered")
else:
    print(f"Average: {total / count}")
    print(f"Product: {product}")