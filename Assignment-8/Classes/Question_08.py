# 8) Write a python class which has 2 methods get_string and print_string. get_string takes a string from the user and print_string prints the string in reverse order 

class Reverse:
    def __init__(self):
        self.string = ''
    
    def get_string(self):
        self.string = input('Enter a string: ')
    
    def print_string(self):
        print(self.string[::-1])

#Test
r = Reverse()
r.get_string()
r.print_string()