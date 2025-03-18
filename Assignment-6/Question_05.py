# 5. Write a Python program to calculate the sum and average of n integer numbers (input from the user). Input 0 to finish

sum = 0
count = 0
while True:
    num = int(input("Enter a number: "))
    if num == 0:
        break
    sum += num
    count += 1
    
if count == 0:
    print("No numbers entered")
else:
    print(f"Sum: {sum}")    
    print(f"Average: {sum / count}")