# 12. A student will not be allowed to sit in exam if his/her attendence is less than 75%.
# Take following input from user
# Number of classes held
# Number of classes attended.
# And print
# percentage of class attended
# Is student is allowed to sit in exam or not.

classes_held = int(input("Number of classes held: "))
classes_attended = int(input("Number of classes attended: "))
attendance = classes_attended / classes_held * 100
if attendance < 75:
    print("Not allowed to sit in exam")
else:
    print("Allowed to sit in exam")