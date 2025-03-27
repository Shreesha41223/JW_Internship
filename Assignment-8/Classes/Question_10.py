# 10) Write a Python program to get the class name of an instance in Python

class ClassName:
    def __init__(self):
        pass

    def get_class_name(self, instance):
        return instance.__class__.__name__
    
class Triangle:
    def __init__(self):
        print('Triangle')

class Rectangle:
    def __init__(self):
        print('Rectangle')

#Test
t = Triangle()
r = Rectangle()
print(ClassName().get_class_name(t))
print(ClassName().get_class_name(r))