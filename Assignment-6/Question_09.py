# 9. A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
# Ask user for quantity
# Suppose, one unit will cost 100.
# Judge and print total cost for user.

quantity = int(input("Quantity: "))
cost = quantity * 100
if cost > 1000:
    cost *= 0.9 

print(f"Total cost: {cost}")