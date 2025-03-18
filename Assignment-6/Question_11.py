# 11. A school has following rules for grading system:
# a. Below 25 - F
# b. 25 to 45 - E
# c. 45 to 50 - D
# d. 50 to 60 - C
# e. 60 to 80 - B
# f. Above 80 - A
# Ask user to enter marks and print the corresponding grade.

marks = int(input("Marks: "))
if marks < 25:
    print("F")
elif marks < 45:
    print("E")
elif marks < 50:
    print("D")
elif marks < 60:
    print("C")
elif marks < 80:
    print("B")
else:
    print("A")