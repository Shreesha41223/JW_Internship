# 8. Take values of length and breadth of a rectangle from user and check if it is square or not.

length = int(input("Length: "))
breadth = int(input("Breadth: "))
if length == breadth:
    print("Square")
else:
    print("Rectangle")