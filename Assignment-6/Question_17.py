# 17. Using range(1,101), make three list, 
# one containing all even numbers
# one containing all odd numbers 
# One containing only prime numbers..

even = []
odd = []
prime = []

for i in range(1, 101):
    if i % 2 == 0:
        even.append(i) 
    else:
        odd.append(i)
    
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            prime.append(i)

print(f"Even numbers: {even}")
print(f"Odd numbers: {odd}")
print(f"Prime numbers: {prime}")
