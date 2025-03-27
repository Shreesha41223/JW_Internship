# 7) Write a Python class to reverse a string word by word. 
# Input string : 'hello .py' Expected Output : '.py hello' 

class Reverse:
    def __init__(self):
        pass

    def reverse_words(self, string):
        return ' '.join(string.split()[::-1])
    
# Test
r = Reverse()
print(r.reverse_words('hello .py'))
print(r.reverse_words('hello world'))